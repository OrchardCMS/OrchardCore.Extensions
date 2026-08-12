#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
CATALOG_ROOTS = ("modules", "themes")
REQUIRED_FIELDS = ("title", "slug", "description", "projectUrl", "nuGetPackageId", "pubDatetime")
URL_FIELDS = ("projectUrl", "documentationUrl")
SLUG_PATTERN = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")
URL_PATTERN = re.compile(r"^https?://[^\s\"']+$")
FEATURE_DESCRIPTION_MIN_LENGTH = 180


def fail(errors, path, message):
    errors.append(f"{path.as_posix()}: {message}")


def split_frontmatter(text):
    if not text.startswith("---\n"):
        return None, None

    end = text.find("\n---", 4)
    if end < 0:
        return None, None

    return text[4:end].strip("\n"), text[end + 4 :].lstrip("\n")


def clean(value):
    value = value.strip()
    if (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")):
        return value[1:-1]
    return value


def parse_frontmatter(frontmatter):
    fields = {}
    lines = frontmatter.splitlines()
    index = 0

    while index < len(lines):
        line = lines[index]
        if not line or line.startswith(" ") or ":" not in line:
            index += 1
            continue

        key, raw_value = line.split(":", 1)
        key = key.strip()
        raw_value = raw_value.strip()

        if raw_value:
            fields[key] = clean(raw_value)
            index += 1
            continue

        block = []
        index += 1
        while index < len(lines) and (lines[index].startswith(" ") or not lines[index].strip()):
            block.append(lines[index])
            index += 1

        fields[key] = "\n".join(block).strip()

    return fields


def parse_author(frontmatter):
    match = re.search(r"^author:\n((?:  .+\n?)+)", frontmatter, re.MULTILINE)
    if not match:
        return {}

    author = {}
    for line in match.group(1).splitlines():
        if ":" in line:
            key, value = line.strip().split(":", 1)
            author[key] = clean(value)

    return author


def parse_features(frontmatter):
    match = re.search(r"^features:\n((?:  .+\n?)+)", frontmatter, re.MULTILINE)
    if not match:
        return []

    features = []
    current = None
    current_key = None

    for line in match.group(1).splitlines():
        if line.startswith("  - "):
            if current:
                features.append(current)
            current = {}
            current_key = None
            remainder = line[4:]
            if ":" in remainder:
                key, value = remainder.split(":", 1)
                current[key.strip()] = clean(value)
            continue

        if current is None:
            continue

        if line.startswith("    ") and not line.startswith("      "):
            stripped = line.strip()
            if ":" not in stripped:
                continue
            key, value = stripped.split(":", 1)
            key = key.strip()
            value = value.strip()
            if value:
                current[key] = clean(value)
                current_key = None
            else:
                current[key] = [] if key == "dependencies" else ""
                current_key = key
            continue

        if line.startswith("      - ") and current_key == "dependencies":
            current[current_key].append(clean(line[8:]))
            continue

        if line.startswith("      ") and current_key:
            value = line.strip()
            if isinstance(current[current_key], list):
                current[current_key].append(clean(value))
            else:
                current[current_key] = (current[current_key] + " " + clean(value)).strip()

    if current:
        features.append(current)

    return features


def validate_entry(path, all_slugs, all_packages, all_features, errors):
    text = path.read_text(encoding="utf-8")
    frontmatter, body = split_frontmatter(text)
    if frontmatter is None:
        fail(errors, path, "missing YAML frontmatter delimited by ---")
        return

    fields = parse_frontmatter(frontmatter)
    author = parse_author(frontmatter)
    features = parse_features(frontmatter)
    relative_parts = path.relative_to(ROOT).parts

    if len(relative_parts) != 3 or relative_parts[0] not in CATALOG_ROOTS:
        fail(errors, path, "entries must live under modules/<Group>/ or themes/<Group>/")
        return

    if not body.strip():
        fail(errors, path, "entry body must not be empty")

    for field in REQUIRED_FIELDS:
        if not fields.get(field):
            fail(errors, path, f"missing required field '{field}'")

    for field in URL_FIELDS:
        value = fields.get(field)
        if value and not URL_PATTERN.match(value):
            fail(errors, path, f"field '{field}' must be an absolute http(s) URL without stray quotes")

    slug = fields.get("slug", "")
    if slug:
        if not SLUG_PATTERN.match(slug):
            fail(errors, path, "slug may only contain letters, numbers, dots, underscores, and hyphens")
        if slug != path.stem:
            fail(errors, path, f"slug '{slug}' must match file name '{path.stem}'")
        if slug in all_slugs:
            fail(errors, path, f"duplicate slug '{slug}' also used by {all_slugs[slug].as_posix()}")
        all_slugs[slug] = path

    package = fields.get("nuGetPackageId", "")
    if package:
        if '"' in package or "'" in package:
            fail(errors, path, "nuGetPackageId must not contain quote characters")
        if package in all_packages:
            fail(errors, path, f"duplicate nuGetPackageId '{package}' also used by {all_packages[package].as_posix()}")
        all_packages[package] = path

    if not author.get("name"):
        fail(errors, path, "missing author.name")

    author_url = author.get("url")
    if not author_url:
        fail(errors, path, "missing author.url")
    elif not URL_PATTERN.match(author_url):
        fail(errors, path, "author.url must be an absolute http(s) URL")

    if relative_parts[0] == "modules":
        if not features:
            fail(errors, path, "module entries must include at least one feature definition")

        for index, feature in enumerate(features, start=1):
            for field in ("id", "name", "description"):
                if not feature.get(field):
                    fail(errors, path, f"feature #{index} missing '{field}'")

            description = feature.get("description", "")
            if description and len(description) < FEATURE_DESCRIPTION_MIN_LENGTH:
                fail(errors, path, f"feature #{index} description must be a paragraph of at least {FEATURE_DESCRIPTION_MIN_LENGTH} characters")

            feature_id = feature.get("id")
            if feature_id:
                if not SLUG_PATTERN.match(feature_id):
                    fail(errors, path, f"feature id '{feature_id}' has invalid characters")
                if feature_id in all_features:
                    fail(errors, path, f"duplicate feature id '{feature_id}' also used by {all_features[feature_id].as_posix()}")
                all_features[feature_id] = path

            dependencies = feature.get("dependencies")
            if dependencies is not None and not isinstance(dependencies, list):
                fail(errors, path, f"feature '{feature_id}' dependencies must be a list")


def main():
    errors = []
    all_slugs = {}
    all_packages = {}
    all_features = {}

    for root in CATALOG_ROOTS:
        root_path = ROOT / root
        if not root_path.exists():
            fail(errors, root_path, "catalog root is missing")
            continue

        for path in sorted(root_path.rglob("*.md")):
            validate_entry(path, all_slugs, all_packages, all_features, errors)

        for path in sorted(root_path.glob("*.md")):
            fail(errors, path, "entries must be grouped by contributor folder")

    if errors:
        print("Catalog validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Catalog validation passed for {len(all_slugs)} entries and {len(all_features)} module features.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

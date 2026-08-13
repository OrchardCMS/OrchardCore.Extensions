# Orchard Core Extensions Gallery Catalog

This repository contains the source catalog for Orchard Core modules and themes published to the Orchard Core extensions gallery. Entries in this repository are automatically published to <https://gallery.orchardcore.net>.

## Folder layout

Catalog entries are grouped by owner so contributors can maintain the modules and themes they manage:

```text
modules/
  CrestApps/
    CrestApps.OrchardCore.AI.md
  Etch/
    Etch.OrchardCore.Fields.md
  Lombiq/
    Lombiq.Walkthroughs.md
  OrchardCore/
    OrchardCore.ContentFields.md
  OrchardCoreContrib/
    OrchardCoreContrib.Contents.md
themes/
  Etch/
    Etch.OrchardCore.AdminTheme.md
  OrchardCore/
    TheAdmin.md
```

Use the existing owner folder when one already exists. Create a new owner folder only when submitting a package from a new maintainer or organization. File names must match the `slug` value exactly.

## Submitting a module or theme

1. Add one Markdown file under `modules/<Owner>/` or `themes/<Owner>/`.
2. Include YAML frontmatter with the required metadata.
3. Include `documentationUrl` when documentation exists for the package. Use the package documentation site, not necessarily a page for a specific feature.
4. For modules, include a `features` list. Add one feature for single-feature modules and one entry per feature for modules that expose multiple Orchard Core features.
5. Add a short Markdown body describing what the package does and link to documentation, samples, or source when useful.
6. Open a pull request. The validation workflow checks folder grouping, duplicate slugs/package IDs, required metadata, URLs, line endings, and module feature definitions.

## Entry format

```markdown
---
title: Example Module
slug: Example.OrchardCore.Module
description:
  Adds example functionality to Orchard Core.
projectUrl: https://github.com/example/Example.OrchardCore.Module
documentationUrl: https://example.com/docs
nuGetPackageId: Example.OrchardCore.Module
tags: ["example"]
author:
  name: Example
  url: https://github.com/example
  imageUrl: https://avatars.githubusercontent.com/u/000000
licenses: [MIT]
dependencies: ["OrchardCore.Contents"]
pubDatetime: 2026-08-12T12:00:00Z
features:
  - id: Example.OrchardCore.Module
    name: Example Module
    description:
      Adds example functionality to Orchard Core.
    category: Content Management
    dependencies:
      - OrchardCore.Contents
---

Describe the package here.
```

Themes use the same metadata but do not need a `features` list.

The required top-level fields are `title`, `slug`, `description`, `projectUrl`, `nuGetPackageId`, and `pubDatetime`. `documentationUrl` is optional, but when present it must be an absolute `http` or `https` URL.

For first-party Orchard Core modules, set `documentationUrl` to <https://docs.orchardcore.net>. For CrestApps modules, set it to <https://orchardcore.crestapps.com>. OrchardCoreContrib package titles should use the `Name (Contrib)` format, such as `Content Localization (Contrib)`.

### Orchard Core version compatibility

Declare which Orchard Core versions a package supports with one of the following optional fields:

- Set `compatibleWithAllVersions: true` when the package supports every Orchard Core version. This is used for modules and themes maintained by The Orchard Core Team.
- Otherwise, list the supported version families under `versions`, one `orchard` entry per family:

  ```yaml
  versions:
    - orchard: 2.x
    - orchard: 3.x
  ```

Use `compatibleWithAllVersions` or `versions`, not both.

## Feature documentation

Feature IDs must match the Orchard Core manifest IDs, not just the assembly or package name. If one package provides several features, document each feature separately with enough detail for gallery search results to explain what the feature does and what problem it solves. Feature descriptions should be full paragraphs; the validator requires at least 180 characters.

For Orchard Core built-in modules and themes, use the official Orchard Core documentation at <https://docs.orchardcore.net/> and the module manifests as the source of truth. CrestApps Orchard Core documentation is available at <https://orchardcore.crestapps.com/> for CrestApps modules and related extensions.

## Validation

Run the same check locally before opening a pull request:

```bash
python3 scripts/validate-catalog.py
```

The PR workflow runs this validator automatically to prevent malformed frontmatter or invalid catalog structure from causing Astro build issues.

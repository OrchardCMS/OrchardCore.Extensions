---
title: Sitemaps
slug: OrchardCore.Sitemaps
description:
  Provides dynamic sitemap generation services.
projectUrl: https://github.com/OrchardCMS/OrchardCore/tree/main/src/OrchardCore.Modules/OrchardCore.Sitemaps
documentationUrl: https://docs.orchardcore.net/en/latest/reference/modules/Sitemaps/
nuGetPackageId: OrchardCore.Sitemaps
tags: ["Orchard Core"]
author:
  name: The Orchard Core Team
  url: https://github.com/OrchardCMS
  imageUrl: https://avatars.githubusercontent.com/u/9933239
licenses: [BSD-3-Clause]
pubDatetime: 2026-08-12T12:00:00Z
features:
  - id: OrchardCore.Sitemaps
    name: Sitemaps
    description: "Provides dynamic sitemap generation services. Its manifest-backed feature ID is `OrchardCore.Sitemaps`, and it is categorized as Content Management. It depends on `OrchardCore.Contents`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Content Management
    dependencies:
      - OrchardCore.Contents
  - id: OrchardCore.Sitemaps.RazorPages
    name: Sitemaps for Decoupled Razor Pages
    description: "Provides decoupled razor pages support for dynamic sitemap generation. Its manifest-backed feature ID is `OrchardCore.Sitemaps.RazorPages`, and it is categorized as Content Management. It depends on `OrchardCore.Sitemaps`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Content Management
    dependencies:
      - OrchardCore.Sitemaps
  - id: OrchardCore.Sitemaps.Cleanup
    name: Sitemaps Cleanup
    description: "Cleanup sitemap cache files through a background task. Its manifest-backed feature ID is `OrchardCore.Sitemaps.Cleanup`, and it is categorized as Content Management. It depends on `OrchardCore.Sitemaps`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Content Management
    dependencies:
      - OrchardCore.Sitemaps
---
Provides dynamic sitemap generation services.

## Features

### Sitemaps

Provides dynamic sitemap generation services. Its manifest-backed feature ID is `OrchardCore.Sitemaps`, and it is categorized as Content Management. It depends on `OrchardCore.Contents`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Sitemaps for Decoupled Razor Pages

Provides decoupled razor pages support for dynamic sitemap generation. Its manifest-backed feature ID is `OrchardCore.Sitemaps.RazorPages`, and it is categorized as Content Management. It depends on `OrchardCore.Sitemaps`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Sitemaps Cleanup

Cleanup sitemap cache files through a background task. Its manifest-backed feature ID is `OrchardCore.Sitemaps.Cleanup`, and it is categorized as Content Management. It depends on `OrchardCore.Sitemaps`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

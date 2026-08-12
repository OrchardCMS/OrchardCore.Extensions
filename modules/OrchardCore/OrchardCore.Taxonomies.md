---
title: Taxonomies
slug: OrchardCore.Taxonomies
description:
  The taxonomies module provides a way to categorize content items. It includes Taxonomies and Taxonomies
  Contents List Filters features in the Content Management area, making the package easier to find when browsing
  related Orchard Core capabilities, dependencies, and documentation.
projectUrl: https://github.com/OrchardCMS/OrchardCore/tree/main/src/OrchardCore.Modules/OrchardCore.Taxonomies
documentationUrl: https://docs.orchardcore.net/en/latest/reference/modules/Taxonomies/
nuGetPackageId: OrchardCore.Taxonomies
tags: ["Orchard Core"]
author:
  name: The Orchard Core Team
  url: https://docs.orchardcore.net
  imageUrl: https://docs.orchardcore.net/en/latest/assets/images/orchard-logo.png
licenses: [BSD-3-Clause]
pubDatetime: 2026-08-12T12:00:00Z
features:
  - id: OrchardCore.Taxonomies
    name: Taxonomies
    description: "The taxonomies module provides a way to categorize content items. Its manifest-backed feature ID is `OrchardCore.Taxonomies`, and it is categorized as Content Management. It depends on `OrchardCore.ContentTypes`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Content Management
    dependencies:
      - OrchardCore.ContentTypes
  - id: OrchardCore.Taxonomies.ContentsAdminList
    name: Taxonomies Contents List Filters
    description: "Provides taxonomy filters in the contents list. Its manifest-backed feature ID is `OrchardCore.Taxonomies.ContentsAdminList`, and it is categorized as Content Management. It depends on `OrchardCore.Taxonomies`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Content Management
    dependencies:
      - OrchardCore.Taxonomies
---
The taxonomies module provides a way to categorize content items.

## Features

### Taxonomies

The taxonomies module provides a way to categorize content items. Its manifest-backed feature ID is `OrchardCore.Taxonomies`, and it is categorized as Content Management. It depends on `OrchardCore.ContentTypes`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Taxonomies Contents List Filters

Provides taxonomy filters in the contents list. Its manifest-backed feature ID is `OrchardCore.Taxonomies.ContentsAdminList`, and it is categorized as Content Management. It depends on `OrchardCore.Taxonomies`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

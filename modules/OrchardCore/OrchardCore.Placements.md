---
title: Placements
slug: OrchardCore.Placements
description:
  The Placements module provides a way to define shape placement in admin UI. It includes Placements and
  Placements file storage features in the Development area, making the package easier to find when browsing
  related Orchard Core capabilities, dependencies, and documentation.
projectUrl: https://github.com/OrchardCMS/OrchardCore/tree/main/src/OrchardCore.Modules/OrchardCore.Placements
documentationUrl: https://docs.orchardcore.net/en/latest/reference/modules/Placements/
nuGetPackageId: OrchardCore.Placements
tags: ["Orchard Core"]
author:
  name: The Orchard Core Team
  url: https://docs.orchardcore.net
  imageUrl: https://docs.orchardcore.net/en/latest/assets/images/favicon.png
licenses: [BSD-3-Clause]
pubDatetime: 2026-08-12T12:00:00Z
features:
  - id: OrchardCore.Placements
    name: Placements
    description: "The Placements module provides a way to define shape placement in admin UI. Its manifest-backed feature ID is `OrchardCore.Placements`, and it is categorized as Development. No additional feature dependencies are listed for it in this catalog entry. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Development
  - id: OrchardCore.Placements.FileStorage
    name: Placements file storage
    description: "Stores Placements in a local file. Its manifest-backed feature ID is `OrchardCore.Placements.FileStorage`, and it is categorized as Development. It depends on `OrchardCore.Placements`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Development
    dependencies:
      - OrchardCore.Placements
---
The Placements module provides a way to define shape placement in admin UI.

## Features

### Placements

The Placements module provides a way to define shape placement in admin UI. Its manifest-backed feature ID is `OrchardCore.Placements`, and it is categorized as Development. No additional feature dependencies are listed for it in this catalog entry. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Placements file storage

Stores Placements in a local file. Its manifest-backed feature ID is `OrchardCore.Placements.FileStorage`, and it is categorized as Development. It depends on `OrchardCore.Placements`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

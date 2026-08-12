---
title: Indexing
slug: OrchardCore.Indexing
description:
  Provides index management. It includes Indexing and Indexing Worker features in the Indexing area, making the
  package easier to find when browsing related Orchard Core capabilities, dependencies, and documentation.
projectUrl: https://github.com/OrchardCMS/OrchardCore/tree/main/src/OrchardCore.Modules/OrchardCore.Indexing
documentationUrl: https://docs.orchardcore.net/en/latest/reference/modules/Indexing/
nuGetPackageId: OrchardCore.Indexing
tags: ["Orchard Core"]
author:
  name: The Orchard Core Team
  url: https://docs.orchardcore.net
  imageUrl: https://docs.orchardcore.net/en/latest/assets/images/orchard-logo.png
licenses: [BSD-3-Clause]
pubDatetime: 2026-08-12T12:00:00Z
features:
  - id: OrchardCore.Indexing
    name: Indexing
    description: "Provides index management. Its manifest-backed feature ID is `OrchardCore.Indexing`, and it is categorized as Indexing. No additional feature dependencies are listed for it in this catalog entry. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Indexing
  - id: OrchardCore.Indexing.Worker
    name: Indexing Worker
    description: "Provides a background task to keep indexes in sync with the latest content item update. Its manifest-backed feature ID is `OrchardCore.Indexing.Worker`, and it is categorized as Indexing. It depends on `OrchardCore.Indexing`, and `OrchardCore.Contents`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Indexing
    dependencies:
      - OrchardCore.Indexing
      - OrchardCore.Contents
---
Provides index management.

## Features

### Indexing

Provides index management. Its manifest-backed feature ID is `OrchardCore.Indexing`, and it is categorized as Indexing. No additional feature dependencies are listed for it in this catalog entry. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Indexing Worker

Provides a background task to keep indexes in sync with the latest content item update. Its manifest-backed feature ID is `OrchardCore.Indexing.Worker`, and it is categorized as Indexing. It depends on `OrchardCore.Indexing`, and `OrchardCore.Contents`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

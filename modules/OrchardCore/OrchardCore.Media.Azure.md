---
title: Azure Media
slug: OrchardCore.Media.Azure
description:
  Enables support for storing media files in Microsoft Azure Blob Storage. It includes Azure Media Storage,
  Azure Media Image Cache and Azure Media Image Cache (Obsolete) features in the Hosting area, making the
  package easier to find when browsing related Orchard Core capabilities, dependencies, and documentation.
projectUrl: https://github.com/OrchardCMS/OrchardCore/tree/main/src/OrchardCore.Modules/OrchardCore.Media.Azure
documentationUrl: https://docs.orchardcore.net
nuGetPackageId: OrchardCore.Media.Azure
tags: ["Orchard Core"]
author:
  name: The Orchard Core Team
  url: https://docs.orchardcore.net
  imageUrl: https://docs.orchardcore.net/en/latest/assets/images/favicon.png
licenses: [BSD-3-Clause]
pubDatetime: 2026-08-12T12:00:00Z
features:
  - id: OrchardCore.Media.Azure.Storage
    name: Azure Media Storage
    description: "Enables support for storing media files in Microsoft Azure Blob Storage. Its manifest-backed feature ID is `OrchardCore.Media.Azure.Storage`, and it is categorized as Hosting. It depends on `OrchardCore.Media.Cache`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Hosting
    dependencies:
      - OrchardCore.Media.Cache
  - id: OrchardCore.Media.Azure.ImageCache
    name: Azure Media Image Cache
    description: "Enables support for storing cached resized images in Microsoft Azure Blob Storage. Its manifest-backed feature ID is `OrchardCore.Media.Azure.ImageCache`, and it is categorized as Hosting. It depends on `OrchardCore.Media`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Hosting
    dependencies:
      - OrchardCore.Media
  - id: OrchardCore.Media.Azure.ImageSharpImageCache
    name: Azure Media Image Cache (Obsolete)
    description: "Obsolete legacy feature ID kept for backwards compatibility. Enables OrchardCore.Media.Azure.ImageCache automatically. Its manifest-backed feature ID is `OrchardCore.Media.Azure.ImageSharpImageCache`, and it is categorized as Hosting. It depends on `OrchardCore.Media.Azure.ImageCache`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Hosting
    dependencies:
      - OrchardCore.Media.Azure.ImageCache
---
Enables support for storing media files in Microsoft Azure Blob Storage.

## Features

### Azure Media Storage

Enables support for storing media files in Microsoft Azure Blob Storage. Its manifest-backed feature ID is `OrchardCore.Media.Azure.Storage`, and it is categorized as Hosting. It depends on `OrchardCore.Media.Cache`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Azure Media Image Cache

Enables support for storing cached resized images in Microsoft Azure Blob Storage. Its manifest-backed feature ID is `OrchardCore.Media.Azure.ImageCache`, and it is categorized as Hosting. It depends on `OrchardCore.Media`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Azure Media Image Cache (Obsolete)

Obsolete legacy feature ID kept for backwards compatibility. Enables OrchardCore.Media.Azure.ImageCache automatically. Its manifest-backed feature ID is `OrchardCore.Media.Azure.ImageSharpImageCache`, and it is categorized as Hosting. It depends on `OrchardCore.Media.Azure.ImageCache`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

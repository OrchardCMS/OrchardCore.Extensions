---
title: Amazon S3 Media
slug: OrchardCore.Media.AmazonS3
description:
  Enables support for storing media files in Amazon S3.
projectUrl: https://github.com/OrchardCMS/OrchardCore/tree/main/src/OrchardCore.Modules/OrchardCore.Media.AmazonS3
documentationUrl: https://docs.orchardcore.net/en/latest/reference/modules/Media.AmazonS3/
nuGetPackageId: OrchardCore.Media.AmazonS3
tags: ["Orchard Core"]
author:
  name: The Orchard Core Team
  url: https://github.com/OrchardCMS
  imageUrl: https://avatars.githubusercontent.com/u/9933239
licenses: [BSD-3-Clause]
pubDatetime: 2026-08-12T12:00:00Z
features:
  - id: OrchardCore.Media.AmazonS3
    name: Amazon Media Storage
    description: "Enables support for storing media files in Amazon S3. Its manifest-backed feature ID is `OrchardCore.Media.AmazonS3`, and it is categorized as Hosting. It depends on `OrchardCore.Media.Cache`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Hosting
    dependencies:
      - OrchardCore.Media.Cache
  - id: OrchardCore.Media.AmazonS3.ImageCache
    name: Amazon Media Image Cache
    description: "Provides storage of cached resized images within the Amazon S3 storage service. Its manifest-backed feature ID is `OrchardCore.Media.AmazonS3.ImageCache`, and it is categorized as Hosting. It depends on `OrchardCore.Media`, and `OrchardCore.Media.AmazonS3`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Hosting
    dependencies:
      - OrchardCore.Media
      - OrchardCore.Media.AmazonS3
  - id: OrchardCore.Media.AmazonS3.ImageSharpImageCache
    name: Amazon Media Image Cache (Obsolete)
    description: "Obsolete legacy feature ID kept for backwards compatibility. Enables OrchardCore.Media.AmazonS3.ImageCache automatically. Its manifest-backed feature ID is `OrchardCore.Media.AmazonS3.ImageSharpImageCache`, and it is categorized as Hosting. It depends on `OrchardCore.Media.AmazonS3.ImageCache`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Hosting
    dependencies:
      - OrchardCore.Media.AmazonS3.ImageCache
---
Enables support for storing media files in Amazon S3.

## Features

### Amazon Media Storage

Enables support for storing media files in Amazon S3. Its manifest-backed feature ID is `OrchardCore.Media.AmazonS3`, and it is categorized as Hosting. It depends on `OrchardCore.Media.Cache`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Amazon Media Image Cache

Provides storage of cached resized images within the Amazon S3 storage service. Its manifest-backed feature ID is `OrchardCore.Media.AmazonS3.ImageCache`, and it is categorized as Hosting. It depends on `OrchardCore.Media`, and `OrchardCore.Media.AmazonS3`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Amazon Media Image Cache (Obsolete)

Obsolete legacy feature ID kept for backwards compatibility. Enables OrchardCore.Media.AmazonS3.ImageCache automatically. Its manifest-backed feature ID is `OrchardCore.Media.AmazonS3.ImageSharpImageCache`, and it is categorized as Hosting. It depends on `OrchardCore.Media.AmazonS3.ImageCache`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

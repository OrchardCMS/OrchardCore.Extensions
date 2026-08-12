---
title: Media
slug: OrchardCore.Media
description:
  The media module adds media management support. It includes Media, Media Indexing and related features in the
  Content Management and Search area, making the package easier to find when browsing related Orchard Core
  capabilities, dependencies, and documentation.
projectUrl: https://github.com/OrchardCMS/OrchardCore/tree/main/src/OrchardCore.Modules/OrchardCore.Media
documentationUrl: https://docs.orchardcore.net
nuGetPackageId: OrchardCore.Media
tags: ["Orchard Core"]
author:
  name: The Orchard Core Team
  url: https://docs.orchardcore.net
  imageUrl: https://docs.orchardcore.net/en/latest/assets/images/favicon.png
licenses: [BSD-3-Clause]
pubDatetime: 2026-08-12T12:00:00Z
features:
  - id: OrchardCore.Media
    name: Media
    description: "The media module adds media management support. Its manifest-backed feature ID is `OrchardCore.Media`, and it is categorized as Content Management. It depends on `OrchardCore.ContentTypes`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Content Management
    dependencies:
      - OrchardCore.ContentTypes
  - id: OrchardCore.Media.Indexing
    name: Media Indexing
    description: "Provides a way to index media files with common format in search providers. Its manifest-backed feature ID is `OrchardCore.Media.Indexing`, and it is categorized as Search. It depends on `OrchardCore.Media`, so Orchard Core enables that dependency when this feature is enabled. The manifest marks it as enabled by dependency only, so it is intended to support other features rather than be selected as a standalone end-user feature. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Search
    dependencies:
      - OrchardCore.Media
    enabledByDependencyOnly: true
  - id: OrchardCore.Media.Indexing.Text
    name: Text Media Indexing
    description: "Provides a way to index common text files like (.txt and .md) in search providers. Its manifest-backed feature ID is `OrchardCore.Media.Indexing.Text`, and it is categorized as Search. It depends on `OrchardCore.Media.Indexing`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Search
    dependencies:
      - OrchardCore.Media.Indexing
  - id: OrchardCore.Media.Cache
    name: Media Cache
    description: "The media cache module adds remote file store cache support. Its manifest-backed feature ID is `OrchardCore.Media.Cache`, and it is categorized as Content Management. It depends on `OrchardCore.Media`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Content Management
    dependencies:
      - OrchardCore.Media
  - id: OrchardCore.Media.Slugify
    name: Media Slugify
    description: "The media slugify module transforms newly created folders and files into SEO-friendly versions by generating slugs. Its manifest-backed feature ID is `OrchardCore.Media.Slugify`, and it is categorized as Content Management. It depends on `OrchardCore.Media`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Content Management
    dependencies:
      - OrchardCore.Media
  - id: OrchardCore.Media.Security
    name: Secure Media
    description: "Adds permissions to restrict access to media folders. Its manifest-backed feature ID is `OrchardCore.Media.Security`, and it is categorized as Content Management. It depends on `OrchardCore.Media`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Content Management
    dependencies:
      - OrchardCore.Media
  - id: OrchardCore.Media.Tus
    name: Media TUS Uploads
    description: "Enables resumable file uploads using the TUS protocol. When enabled, replaces the default chunked upload mechanism with the TUS standard, allowing uploads to be paused and resumed. Its manifest-backed feature ID is `OrchardCore.Media.Tus`, and it is categorized as Content Management. It depends on `OrchardCore.Media`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Content Management
    dependencies:
      - OrchardCore.Media
  - id: OrchardCore.Media.SignalR
    name: Media SignalR
    description: "Enables real-time media updates via SignalR. When enabled, changes to media files and folders are broadcast to connected clients. Its manifest-backed feature ID is `OrchardCore.Media.SignalR`, and it is categorized as Content Management. It depends on `OrchardCore.Media`, and `OrchardCore.SignalR`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Content Management
    dependencies:
      - OrchardCore.Media
      - OrchardCore.SignalR
---
The media module adds media management support.

## Features

### Media

The media module adds media management support. Its manifest-backed feature ID is `OrchardCore.Media`, and it is categorized as Content Management. It depends on `OrchardCore.ContentTypes`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Media Indexing

Provides a way to index media files with common format in search providers. Its manifest-backed feature ID is `OrchardCore.Media.Indexing`, and it is categorized as Search. It depends on `OrchardCore.Media`, so Orchard Core enables that dependency when this feature is enabled. The manifest marks it as enabled by dependency only, so it is intended to support other features rather than be selected as a standalone end-user feature. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Text Media Indexing

Provides a way to index common text files like (.txt and .md) in search providers. Its manifest-backed feature ID is `OrchardCore.Media.Indexing.Text`, and it is categorized as Search. It depends on `OrchardCore.Media.Indexing`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Media Cache

The media cache module adds remote file store cache support. Its manifest-backed feature ID is `OrchardCore.Media.Cache`, and it is categorized as Content Management. It depends on `OrchardCore.Media`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Media Slugify

The media slugify module transforms newly created folders and files into SEO-friendly versions by generating slugs. Its manifest-backed feature ID is `OrchardCore.Media.Slugify`, and it is categorized as Content Management. It depends on `OrchardCore.Media`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Secure Media

Adds permissions to restrict access to media folders. Its manifest-backed feature ID is `OrchardCore.Media.Security`, and it is categorized as Content Management. It depends on `OrchardCore.Media`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Media TUS Uploads

Enables resumable file uploads using the TUS protocol. When enabled, replaces the default chunked upload mechanism with the TUS standard, allowing uploads to be paused and resumed. Its manifest-backed feature ID is `OrchardCore.Media.Tus`, and it is categorized as Content Management. It depends on `OrchardCore.Media`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Media SignalR

Enables real-time media updates via SignalR. When enabled, changes to media files and folders are broadcast to connected clients. Its manifest-backed feature ID is `OrchardCore.Media.SignalR`, and it is categorized as Content Management. It depends on `OrchardCore.Media`, and `OrchardCore.SignalR`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

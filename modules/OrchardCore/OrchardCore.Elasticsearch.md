---
title: Elasticsearch
slug: OrchardCore.Elasticsearch
description:
  Creates Elasticsearch indexes to support search scenarios, introduces a preconfigured container-enabled
  content type. It includes Elasticsearch, Elasticsearch (Obsolete) and related features in the Search area,
  making the package easier to find when browsing related Orchard Core capabilities, dependencies, and
  documentation.
projectUrl: https://github.com/OrchardCMS/OrchardCore/tree/main/src/OrchardCore.Modules/OrchardCore.Elasticsearch
documentationUrl: https://docs.orchardcore.net
nuGetPackageId: OrchardCore.Elasticsearch
tags: ["Orchard Core"]
author:
  name: The Orchard Core Team
  url: https://docs.orchardcore.net
  imageUrl: https://docs.orchardcore.net/en/latest/assets/images/favicon.png
licenses: [BSD-3-Clause]
compatibleWithAllVersions: true
pubDatetime: 2026-08-12T12:00:00Z
features:
  - id: OrchardCore.Elasticsearch
    name: Elasticsearch
    description: "Creates Elasticsearch indexes to support search scenarios, introduces a preconfigured container-enabled content type. Its manifest-backed feature ID is `OrchardCore.Elasticsearch`, and it is categorized as Search. It depends on `OrchardCore.Queries.Core`, `OrchardCore.Indexing`, and `OrchardCore.ContentTypes`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Search
    dependencies:
      - OrchardCore.Queries.Core
      - OrchardCore.Indexing
      - OrchardCore.ContentTypes
  - id: OrchardCore.Search.Elasticsearch
    name: Elasticsearch (Obsolete)
    description: "Obsolete legacy feature ID kept for backwards compatibility. Enables OrchardCore.Elasticsearch automatically. Its manifest-backed feature ID is `OrchardCore.Search.Elasticsearch`, and it is categorized as Search. It depends on `OrchardCore.Elasticsearch`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Search
    dependencies:
      - OrchardCore.Elasticsearch
  - id: OrchardCore.Search.Elasticsearch.Worker
    name: Elasticsearch Worker
    description: "Provides a background task to keep indices in sync with other instances. Its manifest-backed feature ID is `OrchardCore.Search.Elasticsearch.Worker`, and it is categorized as Search. It depends on `OrchardCore.Search.Elasticsearch`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Search
    dependencies:
      - OrchardCore.Search.Elasticsearch
  - id: OrchardCore.Search.Elasticsearch.ContentPicker
    name: Elasticsearch Content Picker
    description: "Provides a Elasticsearch content picker field editor. Its manifest-backed feature ID is `OrchardCore.Search.Elasticsearch.ContentPicker`, and it is categorized as Search. It depends on `OrchardCore.Search.Elasticsearch`, and `OrchardCore.ContentFields`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Search
    dependencies:
      - OrchardCore.Search.Elasticsearch
      - OrchardCore.ContentFields
---
Creates Elasticsearch indexes to support search scenarios, introduces a preconfigured container-enabled content type.

## Features

### Elasticsearch

Creates Elasticsearch indexes to support search scenarios, introduces a preconfigured container-enabled content type. Its manifest-backed feature ID is `OrchardCore.Elasticsearch`, and it is categorized as Search. It depends on `OrchardCore.Queries.Core`, `OrchardCore.Indexing`, and `OrchardCore.ContentTypes`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Elasticsearch (Obsolete)

Obsolete legacy feature ID kept for backwards compatibility. Enables OrchardCore.Elasticsearch automatically. Its manifest-backed feature ID is `OrchardCore.Search.Elasticsearch`, and it is categorized as Search. It depends on `OrchardCore.Elasticsearch`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Elasticsearch Worker

Provides a background task to keep indices in sync with other instances. Its manifest-backed feature ID is `OrchardCore.Search.Elasticsearch.Worker`, and it is categorized as Search. It depends on `OrchardCore.Search.Elasticsearch`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Elasticsearch Content Picker

Provides a Elasticsearch content picker field editor. Its manifest-backed feature ID is `OrchardCore.Search.Elasticsearch.ContentPicker`, and it is categorized as Search. It depends on `OrchardCore.Search.Elasticsearch`, and `OrchardCore.ContentFields`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

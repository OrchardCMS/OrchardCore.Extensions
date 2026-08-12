---
title: Lucene
slug: OrchardCore.Lucene
description:
  Creates Lucene indexes to support search scenarios, introduces a preconfigured container-enabled content type.
projectUrl: https://github.com/OrchardCMS/OrchardCore/tree/main/src/OrchardCore.Modules/OrchardCore.Lucene
documentationUrl: https://docs.orchardcore.net/en/latest/reference/modules/Lucene/
nuGetPackageId: OrchardCore.Lucene
tags: ["Orchard Core"]
author:
  name: The Orchard Core Team
  url: https://github.com/OrchardCMS
  imageUrl: https://avatars.githubusercontent.com/u/9933239
licenses: [BSD-3-Clause]
pubDatetime: 2026-08-12T12:00:00Z
features:
  - id: OrchardCore.Lucene
    name: Lucene
    description: "Creates Lucene indexes to support search scenarios, introduces a preconfigured container-enabled content type. Its manifest-backed feature ID is `OrchardCore.Lucene`, and it is categorized as Search. It depends on `OrchardCore.Queries.Core`, `OrchardCore.Indexing`, and `OrchardCore.ContentTypes`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Search
    dependencies:
      - OrchardCore.Queries.Core
      - OrchardCore.Indexing
      - OrchardCore.ContentTypes
  - id: OrchardCore.Search.Lucene
    name: Lucene (Obsolete)
    description: "Obsolete legacy feature ID kept for backwards compatibility. Enables OrchardCore.Lucene automatically. Its manifest-backed feature ID is `OrchardCore.Search.Lucene`, and it is categorized as Search. It depends on `OrchardCore.Lucene`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Search
    dependencies:
      - OrchardCore.Lucene
  - id: OrchardCore.Search.Lucene.Worker
    name: Lucene Worker
    description: "Provides a background task to keep local indices in sync with other instances. Its manifest-backed feature ID is `OrchardCore.Search.Lucene.Worker`, and it is categorized as Search. It depends on `OrchardCore.Search.Lucene`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Search
    dependencies:
      - OrchardCore.Search.Lucene
  - id: OrchardCore.Search.Lucene.ContentPicker
    name: Lucene Content Picker
    description: "Provides a Lucene content picker field editor. Its manifest-backed feature ID is `OrchardCore.Search.Lucene.ContentPicker`, and it is categorized as Search. It depends on `OrchardCore.Search.Lucene`, and `OrchardCore.ContentFields`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Search
    dependencies:
      - OrchardCore.Search.Lucene
      - OrchardCore.ContentFields
---
Creates Lucene indexes to support search scenarios, introduces a preconfigured container-enabled content type.

## Features

### Lucene

Creates Lucene indexes to support search scenarios, introduces a preconfigured container-enabled content type. Its manifest-backed feature ID is `OrchardCore.Lucene`, and it is categorized as Search. It depends on `OrchardCore.Queries.Core`, `OrchardCore.Indexing`, and `OrchardCore.ContentTypes`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Lucene (Obsolete)

Obsolete legacy feature ID kept for backwards compatibility. Enables OrchardCore.Lucene automatically. Its manifest-backed feature ID is `OrchardCore.Search.Lucene`, and it is categorized as Search. It depends on `OrchardCore.Lucene`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Lucene Worker

Provides a background task to keep local indices in sync with other instances. Its manifest-backed feature ID is `OrchardCore.Search.Lucene.Worker`, and it is categorized as Search. It depends on `OrchardCore.Search.Lucene`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Lucene Content Picker

Provides a Lucene content picker field editor. Its manifest-backed feature ID is `OrchardCore.Search.Lucene.ContentPicker`, and it is categorized as Search. It depends on `OrchardCore.Search.Lucene`, and `OrchardCore.ContentFields`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

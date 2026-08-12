---
title: Azure AI Search
slug: OrchardCore.AzureAI
description:
  Provides Azure AI Search services for managing indexes and facilitating search scenarios within indexes. It
  includes Azure AI Search and Azure AI Search (Obsolete) features in the Search area, making the package easier
  to find when browsing related Orchard Core capabilities, dependencies, and documentation.
projectUrl: https://github.com/OrchardCMS/OrchardCore/tree/main/src/OrchardCore.Modules/OrchardCore.AzureAI
documentationUrl: https://docs.orchardcore.net
nuGetPackageId: OrchardCore.AzureAI
tags: ["Orchard Core"]
author:
  name: The Orchard Core Team
  url: https://docs.orchardcore.net
  imageUrl: https://docs.orchardcore.net/en/latest/assets/images/favicon.png
licenses: [BSD-3-Clause]
pubDatetime: 2026-08-12T12:00:00Z
features:
  - id: OrchardCore.AzureAI
    name: Azure AI Search
    description: "Provides Azure AI Search services for managing indexes and facilitating search scenarios within indexes. Its manifest-backed feature ID is `OrchardCore.AzureAI`, and it is categorized as Search. It depends on `OrchardCore.Indexing`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Search
    dependencies:
      - OrchardCore.Indexing
  - id: OrchardCore.Search.AzureAI
    name: Azure AI Search (Obsolete)
    description: "Obsolete legacy feature ID kept for backwards compatibility. Enables OrchardCore.AzureAI automatically. Its manifest-backed feature ID is `OrchardCore.Search.AzureAI`, and it is categorized as Search. It depends on `OrchardCore.AzureAI`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Search
    dependencies:
      - OrchardCore.AzureAI
---
Provides Azure AI Search services for managing indexes and facilitating search scenarios within indexes.

## Features

### Azure AI Search

Provides Azure AI Search services for managing indexes and facilitating search scenarios within indexes. Its manifest-backed feature ID is `OrchardCore.AzureAI`, and it is categorized as Search. It depends on `OrchardCore.Indexing`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Azure AI Search (Obsolete)

Obsolete legacy feature ID kept for backwards compatibility. Enables OrchardCore.AzureAI automatically. Its manifest-backed feature ID is `OrchardCore.Search.AzureAI`, and it is categorized as Search. It depends on `OrchardCore.AzureAI`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

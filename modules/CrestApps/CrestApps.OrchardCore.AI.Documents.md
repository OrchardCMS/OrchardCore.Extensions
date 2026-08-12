---
title: "AI Documents"
slug: CrestApps.OrchardCore.AI.Documents
description:
  Provides the AI Documents module for Orchard Core. It includes AI Documents, AI Documents for Chat
  Interactions and related features in the Artificial Intelligence - Knowledgebase area, making the package
  easier to find when browsing related Orchard Core capabilities, dependencies, and documentation.
projectUrl: https://github.com/CrestApps/CrestApps.OrchardCore/tree/main/src/Modules/CrestApps.OrchardCore.AI.Documents
documentationUrl: https://orchardcore.crestapps.com/docs/ai/documents/
nuGetPackageId: CrestApps.OrchardCore.AI.Documents
tags: ["crestapps"]
author:
  name: CrestApps
  url: https://crestapps.com
  imageUrl: https://avatars.githubusercontent.com/u/111536479
licenses: [MIT]
pubDatetime: 2026-08-12T12:00:00Z
features:
  - id: CrestApps.OrchardCore.AI.Documents
    name: "AI Documents"
    description: "Provides the foundation for document processing, text extraction, and Retrieval-Augmented Generation (RAG) capabilities. Its manifest-backed feature ID is `CrestApps.OrchardCore.AI.Documents`, and it is categorized as Artificial Intelligence - Knowledgebase. It depends on `CrestApps.OrchardCore.AI.Chat.Interactions`, and `OrchardCore.Indexing`, so Orchard Core enables those dependencies when this feature is enabled. The manifest marks it as enabled by dependency only, so it is intended to support other features rather than be selected as a standalone end-user feature. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: "Artificial Intelligence - Knowledgebase"
    dependencies:
      - CrestApps.OrchardCore.AI.Chat.Interactions
      - OrchardCore.Indexing
    enabledByDependencyOnly: true
  - id: CrestApps.OrchardCore.AI.Documents.ChatInteractions
    name: "AI Documents for Chat Interactions"
    description: "Provides document upload and Retrieval-Augmented Generation (RAG) support for AI Chat Interactions. Its manifest-backed feature ID is `CrestApps.OrchardCore.AI.Documents.ChatInteractions`, and it is categorized as Artificial Intelligence - Knowledgebase. It depends on `CrestApps.OrchardCore.AI.Documents`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: "Artificial Intelligence - Knowledgebase"
    dependencies:
      - CrestApps.OrchardCore.AI.Documents
  - id: CrestApps.OrchardCore.AI.Documents.Profiles
    name: "AI Documents for Profiles"
    description: "Provides document upload and Retrieval-Augmented Generation (RAG) support for AI Profiles. Its manifest-backed feature ID is `CrestApps.OrchardCore.AI.Documents.Profiles`, and it is categorized as Artificial Intelligence - Knowledgebase. It depends on `CrestApps.OrchardCore.AI.Documents`, and `CrestApps.OrchardCore.AI.Chat.Core`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: "Artificial Intelligence - Knowledgebase"
    dependencies:
      - CrestApps.OrchardCore.AI.Documents
      - CrestApps.OrchardCore.AI.Chat.Core
  - id: CrestApps.OrchardCore.AI.Documents.ChatSessions
    name: "AI Documents for Chat Sessions"
    description: "Provides document upload and Retrieval-Augmented Generation (RAG) support for AI Chat Sessions and Widgets. Its manifest-backed feature ID is `CrestApps.OrchardCore.AI.Documents.ChatSessions`, and it is categorized as Artificial Intelligence - Knowledgebase. It depends on `CrestApps.OrchardCore.AI.Documents`, and `CrestApps.OrchardCore.AI.Chat`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: "Artificial Intelligence - Knowledgebase"
    dependencies:
      - CrestApps.OrchardCore.AI.Documents
      - CrestApps.OrchardCore.AI.Chat
---
Provides the AI Documents module for Orchard Core.

## Features

### AI Documents

Provides the foundation for document processing, text extraction, and Retrieval-Augmented Generation (RAG) capabilities. Its manifest-backed feature ID is `CrestApps.OrchardCore.AI.Documents`, and it is categorized as Artificial Intelligence - Knowledgebase. It depends on `CrestApps.OrchardCore.AI.Chat.Interactions`, and `OrchardCore.Indexing`, so Orchard Core enables those dependencies when this feature is enabled. The manifest marks it as enabled by dependency only, so it is intended to support other features rather than be selected as a standalone end-user feature. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### AI Documents for Chat Interactions

Provides document upload and Retrieval-Augmented Generation (RAG) support for AI Chat Interactions. Its manifest-backed feature ID is `CrestApps.OrchardCore.AI.Documents.ChatInteractions`, and it is categorized as Artificial Intelligence - Knowledgebase. It depends on `CrestApps.OrchardCore.AI.Documents`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### AI Documents for Profiles

Provides document upload and Retrieval-Augmented Generation (RAG) support for AI Profiles. Its manifest-backed feature ID is `CrestApps.OrchardCore.AI.Documents.Profiles`, and it is categorized as Artificial Intelligence - Knowledgebase. It depends on `CrestApps.OrchardCore.AI.Documents`, and `CrestApps.OrchardCore.AI.Chat.Core`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### AI Documents for Chat Sessions

Provides document upload and Retrieval-Augmented Generation (RAG) support for AI Chat Sessions and Widgets. Its manifest-backed feature ID is `CrestApps.OrchardCore.AI.Documents.ChatSessions`, and it is categorized as Artificial Intelligence - Knowledgebase. It depends on `CrestApps.OrchardCore.AI.Documents`, and `CrestApps.OrchardCore.AI.Chat`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

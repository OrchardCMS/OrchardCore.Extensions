---
title: "Artificial Intelligence"
slug: CrestApps.OrchardCore.AI
description:
  Provides the Artificial Intelligence module for Orchard Core. It includes AI Services, AI Chat Services and
  related features in the Artificial Intelligence area, making the package easier to find when browsing related
  Orchard Core capabilities, dependencies, and documentation.
projectUrl: https://github.com/CrestApps/CrestApps.OrchardCore/tree/main/src/Modules/CrestApps.OrchardCore.AI
documentationUrl: https://orchardcore.crestapps.com/docs/ai/overview
nuGetPackageId: CrestApps.OrchardCore.AI
tags: ["crestapps"]
author:
  name: CrestApps
  url: https://crestapps.com
  imageUrl: https://avatars.githubusercontent.com/u/111536479
licenses: [MIT]
pubDatetime: 2026-08-12T12:00:00Z
features:
  - id: CrestApps.OrchardCore.AI
    name: "AI Services"
    description: "Provides AI services. Its manifest-backed feature ID is `CrestApps.OrchardCore.AI`, and it is categorized as Artificial Intelligence. It depends on `CrestApps.OrchardCore.Resources`, so Orchard Core enables that dependency when this feature is enabled. The manifest marks it as enabled by dependency only, so it is intended to support other features rather than be selected as a standalone end-user feature. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: "Artificial Intelligence"
    dependencies:
      - CrestApps.OrchardCore.Resources
    enabledByDependencyOnly: true
  - id: CrestApps.OrchardCore.AI.Chat.Core
    name: "AI Chat Services"
    description: "Provides all the necessary services to enable chatting with AI models using profiles. Its manifest-backed feature ID is `CrestApps.OrchardCore.AI.Chat.Core`, and it is categorized as Artificial Intelligence. It depends on `OrchardCore.Liquid`, `CrestApps.OrchardCore.Resources`, `CrestApps.OrchardCore.AI.Prompting`, and `CrestApps.OrchardCore.AI`, so Orchard Core enables those dependencies when this feature is enabled. The manifest marks it as enabled by dependency only, so it is intended to support other features rather than be selected as a standalone end-user feature. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: "Artificial Intelligence"
    dependencies:
      - OrchardCore.Liquid
      - CrestApps.OrchardCore.Resources
      - CrestApps.OrchardCore.AI.Prompting
      - CrestApps.OrchardCore.AI
    enabledByDependencyOnly: true
  - id: CrestApps.OrchardCore.AI.Chat.Api
    name: "AI Chat WebAPI"
    description: "Provides a RESTful API for interacting with the AI chat. Its manifest-backed feature ID is `CrestApps.OrchardCore.AI.Chat.Api`, and it is categorized as Artificial Intelligence. It depends on `CrestApps.OrchardCore.AI.Chat.Core`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: "Artificial Intelligence"
    dependencies:
      - CrestApps.OrchardCore.AI.Chat.Core
  - id: CrestApps.OrchardCore.AI.ConnectionManagement
    name: "AI Connection Management"
    description: "Provides user interface to manage AI connections. Its manifest-backed feature ID is `CrestApps.OrchardCore.AI.ConnectionManagement`, and it is categorized as Artificial Intelligence. It depends on `CrestApps.OrchardCore.AI`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: "Artificial Intelligence"
    dependencies:
      - CrestApps.OrchardCore.AI
  - id: CrestApps.OrchardCore.AI.ToolInstances
    name: "AI Tool Instances"
    description: "Provides user interface to manage AI tool instances. Its manifest-backed feature ID is `CrestApps.OrchardCore.AI.ToolInstances`, and it is categorized as Artificial Intelligence. It depends on `CrestApps.OrchardCore.AI`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: "Artificial Intelligence"
    dependencies:
      - CrestApps.OrchardCore.AI
    documentationUrl: https://orchardcore.crestapps.com/docs/ai/tool-instances
---
Provides the Artificial Intelligence module for Orchard Core.

## Features

### AI Services

Provides AI services. Its manifest-backed feature ID is `CrestApps.OrchardCore.AI`, and it is categorized as Artificial Intelligence. It depends on `CrestApps.OrchardCore.Resources`, so Orchard Core enables that dependency when this feature is enabled. The manifest marks it as enabled by dependency only, so it is intended to support other features rather than be selected as a standalone end-user feature. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### AI Chat Services

Provides all the necessary services to enable chatting with AI models using profiles. Its manifest-backed feature ID is `CrestApps.OrchardCore.AI.Chat.Core`, and it is categorized as Artificial Intelligence. It depends on `OrchardCore.Liquid`, `CrestApps.OrchardCore.Resources`, `CrestApps.OrchardCore.AI.Prompting`, and `CrestApps.OrchardCore.AI`, so Orchard Core enables those dependencies when this feature is enabled. The manifest marks it as enabled by dependency only, so it is intended to support other features rather than be selected as a standalone end-user feature. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### AI Chat WebAPI

Provides a RESTful API for interacting with the AI chat. Its manifest-backed feature ID is `CrestApps.OrchardCore.AI.Chat.Api`, and it is categorized as Artificial Intelligence. It depends on `CrestApps.OrchardCore.AI.Chat.Core`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### AI Connection Management

Provides user interface to manage AI connections. Its manifest-backed feature ID is `CrestApps.OrchardCore.AI.ConnectionManagement`, and it is categorized as Artificial Intelligence. It depends on `CrestApps.OrchardCore.AI`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### AI Tool Instances

Provides user interface to manage AI tool instances. Its manifest-backed feature ID is `CrestApps.OrchardCore.AI.ToolInstances`, and it is categorized as Artificial Intelligence. It depends on `CrestApps.OrchardCore.AI`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

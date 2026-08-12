---
title: "Artificial Intelligence - Chat"
slug: CrestApps.OrchardCore.AI.Chat
description:
  Provides the Artificial Intelligence module for Orchard Core. It includes AI Chat, AI Chat Admin Widget and AI
  Chat Session Analytics features in the Artificial Intelligence area, making the package easier to find when
  browsing related Orchard Core capabilities, dependencies, and documentation.
projectUrl: https://github.com/CrestApps/CrestApps.OrchardCore/tree/main/src/Modules/CrestApps.OrchardCore.AI.Chat
documentationUrl: https://orchardcore.crestapps.com/docs/ai/chat-notifications
nuGetPackageId: CrestApps.OrchardCore.AI.Chat
tags: ["crestapps"]
author:
  name: CrestApps
  url: https://crestapps.com
  imageUrl: https://avatars.githubusercontent.com/u/111536479
licenses: [MIT]
pubDatetime: 2026-08-12T18:03:00Z
features:
  - id: CrestApps.OrchardCore.AI.Chat
    name: "AI Chat"
    description: "Provides UI to interact with AI models using the profiles. Its manifest-backed feature ID is `CrestApps.OrchardCore.AI.Chat`, and it is categorized as Artificial Intelligence. It depends on `OrchardCore.Liquid`, `CrestApps.OrchardCore.Resources`, `CrestApps.OrchardCore.AI.Chat.Core`, `CrestApps.OrchardCore.SignalR`, and `CrestApps.OrchardCore.AI`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: "Artificial Intelligence"
    dependencies:
      - OrchardCore.Liquid
      - CrestApps.OrchardCore.Resources
      - CrestApps.OrchardCore.AI.Chat.Core
      - CrestApps.OrchardCore.SignalR
      - CrestApps.OrchardCore.AI
  - id: CrestApps.OrchardCore.AI.Chat.AdminWidget
    name: "AI Chat Admin Widget"
    description: "Provides a floating AI chat widget on every admin page, allowing users to interact with a predefined AI profile. Its manifest-backed feature ID is `CrestApps.OrchardCore.AI.Chat.AdminWidget`, and it is categorized as Artificial Intelligence. It depends on `CrestApps.OrchardCore.AI.Chat`, and `CrestApps.OrchardCore.AI.Agent`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: "Artificial Intelligence"
    dependencies:
      - CrestApps.OrchardCore.AI.Chat
      - CrestApps.OrchardCore.AI.Agent
    documentationUrl: https://orchardcore.crestapps.com/docs/ai/chat
  - id: CrestApps.OrchardCore.AI.Chat.Analytics
    name: "AI Chat Session Analytics"
    description: "Tracks chat session usage metrics (unique visitors, handle time, containment rate, abandonment rate) and provides reporting with extensible display drivers. Its manifest-backed feature ID is `CrestApps.OrchardCore.AI.Chat.Analytics`, and it is categorized as Artificial Intelligence. It depends on `CrestApps.OrchardCore.AI.Chat`, and `CrestApps.OrchardCore.AI.Chat.Core`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: "Artificial Intelligence"
    dependencies:
      - CrestApps.OrchardCore.AI.Chat
      - CrestApps.OrchardCore.AI.Chat.Core
    documentationUrl: https://orchardcore.crestapps.com/docs/ai/chat-analytics
---
Provides the Artificial Intelligence module for Orchard Core.

## Features

### AI Chat

Provides UI to interact with AI models using the profiles. Its manifest-backed feature ID is `CrestApps.OrchardCore.AI.Chat`, and it is categorized as Artificial Intelligence. It depends on `OrchardCore.Liquid`, `CrestApps.OrchardCore.Resources`, `CrestApps.OrchardCore.AI.Chat.Core`, `CrestApps.OrchardCore.SignalR`, and `CrestApps.OrchardCore.AI`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### AI Chat Admin Widget

Provides a floating AI chat widget on every admin page, allowing users to interact with a predefined AI profile. Its manifest-backed feature ID is `CrestApps.OrchardCore.AI.Chat.AdminWidget`, and it is categorized as Artificial Intelligence. It depends on `CrestApps.OrchardCore.AI.Chat`, and `CrestApps.OrchardCore.AI.Agent`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### AI Chat Session Analytics

Tracks chat session usage metrics (unique visitors, handle time, containment rate, abandonment rate) and provides reporting with extensible display drivers. Its manifest-backed feature ID is `CrestApps.OrchardCore.AI.Chat.Analytics`, and it is categorized as Artificial Intelligence. It depends on `CrestApps.OrchardCore.AI.Chat`, and `CrestApps.OrchardCore.AI.Chat.Core`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

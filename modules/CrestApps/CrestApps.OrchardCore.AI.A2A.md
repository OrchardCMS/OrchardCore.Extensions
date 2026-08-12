---
title: "Agent-to-Agent (A2A) Protocol"
slug: CrestApps.OrchardCore.AI.A2A
description:
  Provides the Agent-to-Agent (A2A) Protocol module for Orchard Core. It includes Agent-to-Agent (A2A) Client
  and Agent-to-Agent (A2A) Host features in the Artificial Intelligence - A2A area, making the package easier to
  find when browsing related Orchard Core capabilities, dependencies, and documentation.
projectUrl: https://github.com/CrestApps/CrestApps.OrchardCore/tree/main/src/Modules/CrestApps.OrchardCore.AI.A2A
documentationUrl: https://orchardcore.crestapps.com/docs/ai/a2a/
nuGetPackageId: CrestApps.OrchardCore.AI.A2A
tags: ["crestapps"]
author:
  name: The CrestApps Team
  url: https://crestapps.com
  imageUrl: https://avatars.githubusercontent.com/u/111536479?s=400&u=d9bdde0365d02b3ed9184034accb696cb12863c5&v=4
licenses: [MIT]
pubDatetime: 2026-08-12T12:00:00Z
features:
  - id: CrestApps.OrchardCore.AI.A2A
    name: "Agent-to-Agent (A2A) Client"
    description: "Provides a user interface for connecting to remote Agent-to-Agent (A2A) hosts, enabling AI profiles to leverage external agents for multi-agent orchestration. Its manifest-backed feature ID is `CrestApps.OrchardCore.AI.A2A`, and it is categorized as Artificial Intelligence - A2A. It depends on `CrestApps.OrchardCore.AI`, and `CrestApps.OrchardCore.Resources`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: "Artificial Intelligence - A2A"
    dependencies:
      - CrestApps.OrchardCore.AI
      - CrestApps.OrchardCore.Resources
  - id: CrestApps.OrchardCore.AI.A2A.Host
    name: "Agent-to-Agent (A2A) Host"
    description: "Exposes all AI Agent profiles through the A2A protocol, enabling external agents and clients to discover and communicate with locally hosted agents. Its manifest-backed feature ID is `CrestApps.OrchardCore.AI.A2A.Host`, and it is categorized as Artificial Intelligence - A2A. It depends on `CrestApps.OrchardCore.AI`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: "Artificial Intelligence - A2A"
    dependencies:
      - CrestApps.OrchardCore.AI
    documentationUrl: https://orchardcore.crestapps.com/docs/ai/a2a/host
---
Provides the Agent-to-Agent (A2A) Protocol module for Orchard Core.

## Features

### Agent-to-Agent (A2A) Client

Provides a user interface for connecting to remote Agent-to-Agent (A2A) hosts, enabling AI profiles to leverage external agents for multi-agent orchestration. Its manifest-backed feature ID is `CrestApps.OrchardCore.AI.A2A`, and it is categorized as Artificial Intelligence - A2A. It depends on `CrestApps.OrchardCore.AI`, and `CrestApps.OrchardCore.Resources`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Agent-to-Agent (A2A) Host

Exposes all AI Agent profiles through the A2A protocol, enabling external agents and clients to discover and communicate with locally hosted agents. Its manifest-backed feature ID is `CrestApps.OrchardCore.AI.A2A.Host`, and it is categorized as Artificial Intelligence - A2A. It depends on `CrestApps.OrchardCore.AI`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

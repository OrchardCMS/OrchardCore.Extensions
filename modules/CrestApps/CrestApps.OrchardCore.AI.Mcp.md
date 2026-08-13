---
title: "Model Context Protocol (MCP) Client"
slug: CrestApps.OrchardCore.AI.Mcp
description:
  Provides the Model Context Protocol (MCP) Client module for Orchard Core. It includes Model Context Protocol
  (MCP) Client, Model Context Protocol (MCP) Local Client and Model Context Protocol (MCP) Server features in
  the Artificial Intelligence - MCP area, making the package easier to find when browsing related Orchard Core
  capabilities, dependencies, and documentation.
projectUrl: https://github.com/CrestApps/CrestApps.OrchardCore/tree/main/src/Modules/CrestApps.OrchardCore.AI.Mcp
documentationUrl: https://orchardcore.crestapps.com
nuGetPackageId: CrestApps.OrchardCore.AI.Mcp
tags: ["crestapps"]
author:
  name: CrestApps
  url: https://crestapps.com
  imageUrl: https://avatars.githubusercontent.com/u/111536479
licenses: [MIT]
versions:
  - 2.x
  - 3.x
pubDatetime: 2026-08-12T12:00:00Z
features:
  - id: CrestApps.OrchardCore.AI.Mcp
    name: "Model Context Protocol (MCP) Client"
    description: "Offers core services and a user interface for connecting to Model Context Protocol (MCP) servers, enabling AI models to leverage additional capabilities and resources. Its manifest-backed feature ID is `CrestApps.OrchardCore.AI.Mcp`, and it is categorized as Artificial Intelligence - MCP. It depends on `CrestApps.OrchardCore.AI`, and `CrestApps.OrchardCore.Resources`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: "Artificial Intelligence - MCP"
    dependencies:
      - CrestApps.OrchardCore.AI
      - CrestApps.OrchardCore.Resources
  - id: CrestApps.OrchardCore.AI.Mcp.Stdio
    name: "Model Context Protocol (MCP) Local Client"
    description: "Extends the Model Context Protocol Client with standard input/output (STDIO) transport for connecting to local MCP servers. Its manifest-backed feature ID is `CrestApps.OrchardCore.AI.Mcp.Stdio`, and it is categorized as Artificial Intelligence - MCP. It depends on `CrestApps.OrchardCore.AI.Mcp`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: "Artificial Intelligence - MCP"
    dependencies:
      - CrestApps.OrchardCore.AI.Mcp
    documentationUrl: https://orchardcore.crestapps.com/docs/ai/mcp/client
  - id: CrestApps.OrchardCore.AI.Mcp.Server
    name: "Model Context Protocol (MCP) Server"
    description: "Exposes Orchard Core AI tools through the MCP protocol, enabling external MCP-compatible clients to connect and invoke AI capabilities. Its manifest-backed feature ID is `CrestApps.OrchardCore.AI.Mcp.Server`, and it is categorized as Artificial Intelligence - MCP. It depends on `CrestApps.OrchardCore.AI`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: "Artificial Intelligence - MCP"
    dependencies:
      - CrestApps.OrchardCore.AI
    documentationUrl: https://orchardcore.crestapps.com/docs/ai/mcp/server
---
Provides the Model Context Protocol (MCP) Client module for Orchard Core.

## Features

### Model Context Protocol (MCP) Client

Offers core services and a user interface for connecting to Model Context Protocol (MCP) servers, enabling AI models to leverage additional capabilities and resources. Its manifest-backed feature ID is `CrestApps.OrchardCore.AI.Mcp`, and it is categorized as Artificial Intelligence - MCP. It depends on `CrestApps.OrchardCore.AI`, and `CrestApps.OrchardCore.Resources`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Model Context Protocol (MCP) Local Client

Extends the Model Context Protocol Client with standard input/output (STDIO) transport for connecting to local MCP servers. Its manifest-backed feature ID is `CrestApps.OrchardCore.AI.Mcp.Stdio`, and it is categorized as Artificial Intelligence - MCP. It depends on `CrestApps.OrchardCore.AI.Mcp`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Model Context Protocol (MCP) Server

Exposes Orchard Core AI tools through the MCP protocol, enabling external MCP-compatible clients to connect and invoke AI capabilities. Its manifest-backed feature ID is `CrestApps.OrchardCore.AI.Mcp.Server`, and it is categorized as Artificial Intelligence - MCP. It depends on `CrestApps.OrchardCore.AI`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

---
title: Workflows
slug: OrchardCore.Workflows
description:
  The Workflows module provides tools and APIs to create custom workflows
projectUrl: https://github.com/OrchardCMS/OrchardCore/tree/main/src/OrchardCore.Modules/OrchardCore.Workflows
documentationUrl: https://docs.orchardcore.net/en/latest/reference/modules/Workflows/
nuGetPackageId: OrchardCore.Workflows
tags: ["Orchard Core", "Workflows"]
author:
  name: The Orchard Core Team
  url: https://github.com/OrchardCMS
  imageUrl: https://avatars.githubusercontent.com/u/9933239
licenses: [BSD-3-Clause]
pubDatetime: 2026-08-12T12:00:00Z
features:
  - id: OrchardCore.Workflows
    name: Workflows
    description: "The Workflows module provides tools and APIs to create custom workflows. Its manifest-backed feature ID is `OrchardCore.Workflows`, and it is categorized as Workflows. It depends on `OrchardCore.Liquid`, and `OrchardCore.Scripting`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Workflows
    dependencies:
      - OrchardCore.Liquid
      - OrchardCore.Scripting
  - id: OrchardCore.Workflows.Http
    name: HTTP Workflows Activities
    description: "Provides HTTP-related services and activities. Its manifest-backed feature ID is `OrchardCore.Workflows.Http`, and it is categorized as Workflows. It depends on `OrchardCore.Workflows`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Workflows
    dependencies:
      - OrchardCore.Workflows
  - id: OrchardCore.Workflows.Timers
    name: Timer Workflows Activities
    description: "Provides timer-based services and activities. Its manifest-backed feature ID is `OrchardCore.Workflows.Timers`, and it is categorized as Workflows. It depends on `OrchardCore.Workflows`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Workflows
    dependencies:
      - OrchardCore.Workflows
  - id: OrchardCore.Workflows.Session
    name: Session Workflows Activities
    description: "Provides 'YesSql' Session-related activities. Its manifest-backed feature ID is `OrchardCore.Workflows.Session`, and it is categorized as Workflows. It depends on `OrchardCore.Workflows`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Workflows
    dependencies:
      - OrchardCore.Workflows
---
The Workflows module provides tools and APIs to create custom workflows

## Features

### Workflows

The Workflows module provides tools and APIs to create custom workflows. Its manifest-backed feature ID is `OrchardCore.Workflows`, and it is categorized as Workflows. It depends on `OrchardCore.Liquid`, and `OrchardCore.Scripting`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### HTTP Workflows Activities

Provides HTTP-related services and activities. Its manifest-backed feature ID is `OrchardCore.Workflows.Http`, and it is categorized as Workflows. It depends on `OrchardCore.Workflows`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Timer Workflows Activities

Provides timer-based services and activities. Its manifest-backed feature ID is `OrchardCore.Workflows.Timers`, and it is categorized as Workflows. It depends on `OrchardCore.Workflows`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Session Workflows Activities

Provides 'YesSql' Session-related activities. Its manifest-backed feature ID is `OrchardCore.Workflows.Session`, and it is categorized as Workflows. It depends on `OrchardCore.Workflows`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

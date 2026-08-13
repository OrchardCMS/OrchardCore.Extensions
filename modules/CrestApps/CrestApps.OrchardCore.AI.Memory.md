---
title: "AI Memory"
slug: CrestApps.OrchardCore.AI.Memory
description:
  Provides the AI Memory module for Orchard Core. It helps site owners add this capability to Orchard Core sites
  while exposing package, dependency, and documentation details in the extensions gallery.
projectUrl: https://github.com/CrestApps/CrestApps.OrchardCore/tree/main/src/Modules/CrestApps.OrchardCore.AI.Memory
documentationUrl: https://orchardcore.crestapps.com
nuGetPackageId: CrestApps.OrchardCore.AI.Memory
tags: ["crestapps"]
author:
  name: CrestApps
  url: https://crestapps.com
  imageUrl: https://avatars.githubusercontent.com/u/111536479
licenses: [MIT]
versions:
  - orchard: 2.x
  - orchard: 3.x
pubDatetime: 2026-08-12T12:00:00Z
features:
  - id: CrestApps.OrchardCore.AI.Memory
    name: "AI Memory"
    description: "Provides persistent, user-scoped AI memory for AI profiles and chat interactions. Its manifest-backed feature ID is `CrestApps.OrchardCore.AI.Memory`, and it is categorized as Artificial Intelligence - Knowledgebase. It depends on `CrestApps.OrchardCore.AI.Chat.Core`, and `OrchardCore.Indexing`, so Orchard Core enables those dependencies when this feature is enabled. The manifest marks it as enabled by dependency only, so it is intended to support other features rather than be selected as a standalone end-user feature. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: "Artificial Intelligence - Knowledgebase"
    dependencies:
      - CrestApps.OrchardCore.AI.Chat.Core
      - OrchardCore.Indexing
    enabledByDependencyOnly: true
---
Provides the AI Memory module for Orchard Core.

## Features

### AI Memory

Provides persistent, user-scoped AI memory for AI profiles and chat interactions. Its manifest-backed feature ID is `CrestApps.OrchardCore.AI.Memory`, and it is categorized as Artificial Intelligence - Knowledgebase. It depends on `CrestApps.OrchardCore.AI.Chat.Core`, and `OrchardCore.Indexing`, so Orchard Core enables those dependencies when this feature is enabled. The manifest marks it as enabled by dependency only, so it is intended to support other features rather than be selected as a standalone end-user feature. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

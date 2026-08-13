---
title: "CrestApps SignalR Redis Backplane"
slug: CrestApps.OrchardCore.SignalR.Redis
description:
  Routes SignalR messages across application nodes through a tenant-qualified Redis backplane. It helps site
  owners add this capability to Orchard Core sites while exposing package, dependency, and documentation details
  in the extensions gallery.
projectUrl: https://github.com/CrestApps/CrestApps.OrchardCore/tree/main/src/Modules/CrestApps.OrchardCore.SignalR.Redis
documentationUrl: https://orchardcore.crestapps.com
nuGetPackageId: CrestApps.OrchardCore.SignalR.Redis
tags: ["crestapps", "Communication"]
author:
  name: CrestApps
  url: https://crestapps.com
  imageUrl: https://avatars.githubusercontent.com/u/111536479
licenses: [MIT]
dependencies: ["CrestApps.OrchardCore.SignalR", "OrchardCore.Redis"]
versions:
  - orchard: 2.x
  - orchard: 3.x
pubDatetime: 2026-08-12T12:00:00Z
features:
  - id: CrestApps.OrchardCore.SignalR.Redis
    name: "SignalR Redis Backplane"
    description: "Routes SignalR messages across application nodes through a tenant-qualified Redis backplane. Its manifest-backed feature ID is `CrestApps.OrchardCore.SignalR.Redis`, and it is categorized as Communication. It depends on `CrestApps.OrchardCore.SignalR`, and `OrchardCore.Redis`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: "Communication"
    dependencies:
      - CrestApps.OrchardCore.SignalR
      - OrchardCore.Redis
---
Routes SignalR messages across application nodes through a tenant-qualified Redis backplane.

## Features

### SignalR Redis Backplane

Routes SignalR messages across application nodes through a tenant-qualified Redis backplane. Its manifest-backed feature ID is `CrestApps.OrchardCore.SignalR.Redis`, and it is categorized as Communication. It depends on `CrestApps.OrchardCore.SignalR`, and `OrchardCore.Redis`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

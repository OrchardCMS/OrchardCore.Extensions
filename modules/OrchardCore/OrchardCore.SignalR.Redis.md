---
title: SignalR Redis Backplane
slug: OrchardCore.SignalR.Redis
description:
  Routes SignalR messages across application nodes through a tenant-qualified Redis backplane.
projectUrl: https://github.com/OrchardCMS/OrchardCore/tree/main/src/OrchardCore.Modules/OrchardCore.SignalR.Redis
documentationUrl: https://docs.orchardcore.net/en/latest/reference/modules/SignalR.Redis/
nuGetPackageId: OrchardCore.SignalR.Redis
tags: ["Orchard Core", "Infrastructure"]
author:
  name: The Orchard Core Team
  url: https://github.com/OrchardCMS
  imageUrl: https://avatars.githubusercontent.com/u/9933239
licenses: [BSD-3-Clause]
pubDatetime: 2026-08-12T12:00:00Z
features:
  - id: OrchardCore.SignalR.Redis
    name: SignalR Redis Backplane
    description: "Uses Redis as the SignalR backplane, enabling multi-instance deployments with a tenant-qualified channel prefix. Its manifest-backed feature ID is `OrchardCore.SignalR.Redis`, and it is categorized as Infrastructure. It depends on `OrchardCore.SignalR`, and `OrchardCore.Redis`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Infrastructure
    dependencies:
      - OrchardCore.SignalR
      - OrchardCore.Redis
---
Routes SignalR messages across application nodes through a tenant-qualified Redis backplane.

## Features

### SignalR Redis Backplane

Uses Redis as the SignalR backplane, enabling multi-instance deployments with a tenant-qualified channel prefix. Its manifest-backed feature ID is `OrchardCore.SignalR.Redis`, and it is categorized as Infrastructure. It depends on `OrchardCore.SignalR`, and `OrchardCore.Redis`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

---
title: SignalR Azure Backplane
slug: OrchardCore.SignalR.Azure
description:
  Routes SignalR messages across application nodes through the Azure SignalR Service. It helps site owners add
  this capability to Orchard Core sites while exposing package, dependency, and documentation details in the
  extensions gallery.
projectUrl: https://github.com/OrchardCMS/OrchardCore/tree/main/src/OrchardCore.Modules/OrchardCore.SignalR.Azure
documentationUrl: https://docs.orchardcore.net
nuGetPackageId: OrchardCore.SignalR.Azure
tags: ["Orchard Core", "Infrastructure"]
author:
  name: The Orchard Core Team
  url: https://docs.orchardcore.net
  imageUrl: https://docs.orchardcore.net/en/latest/assets/images/favicon.png
licenses: [BSD-3-Clause]
pubDatetime: 2026-08-12T12:00:00Z
features:
  - id: OrchardCore.SignalR.Azure
    name: SignalR Azure Backplane
    description: "Uses the Azure SignalR Service as the SignalR backplane, enabling multi-instance deployments. Its manifest-backed feature ID is `OrchardCore.SignalR.Azure`, and it is categorized as Infrastructure. It depends on `OrchardCore.SignalR`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Infrastructure
    dependencies:
      - OrchardCore.SignalR
---
Routes SignalR messages across application nodes through the Azure SignalR Service.

## Features

### SignalR Azure Backplane

Uses the Azure SignalR Service as the SignalR backplane, enabling multi-instance deployments. Its manifest-backed feature ID is `OrchardCore.SignalR.Azure`, and it is categorized as Infrastructure. It depends on `OrchardCore.SignalR`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

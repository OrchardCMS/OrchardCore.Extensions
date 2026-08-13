---
title: "Telephony"
slug: CrestApps.OrchardCore.Telephony
description:
  Provides a provider-agnostic soft phone and SignalR hub for integrating telephony providers. It includes
  Telephony, Telephony Administration and Telephony Soft Phone features in the Telephony area, making the
  package easier to find when browsing related Orchard Core capabilities, dependencies, and documentation.
projectUrl: https://github.com/CrestApps/CrestApps.OrchardCore/tree/main/src/Modules/CrestApps.OrchardCore.Telephony
documentationUrl: https://orchardcore.crestapps.com
nuGetPackageId: CrestApps.OrchardCore.Telephony
tags: ["crestapps", "Telephony"]
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
  - id: CrestApps.OrchardCore.Telephony
    name: "Telephony"
    description: "Provides the provider-agnostic telephony services, SignalR hub, and site settings. Its manifest-backed feature ID is `CrestApps.OrchardCore.Telephony`, and it is categorized as Telephony. It depends on `OrchardCore.Users`, and `CrestApps.OrchardCore.SignalR`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: "Telephony"
    dependencies:
      - OrchardCore.Users
      - CrestApps.OrchardCore.SignalR
  - id: CrestApps.OrchardCore.Telephony.Admin
    name: "Telephony Administration"
    description: "Adds the telephony provider settings screen and its administration menu entry. Its manifest-backed feature ID is `CrestApps.OrchardCore.Telephony.Admin`, and it is categorized as Telephony. It depends on `CrestApps.OrchardCore.Telephony`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: "Telephony"
    dependencies:
      - CrestApps.OrchardCore.Telephony
  - id: CrestApps.OrchardCore.Telephony.SoftPhone
    name: "Telephony Soft Phone"
    description: "Injects the floating soft phone experience into the admin dashboard, front end, or both. Its manifest-backed feature ID is `CrestApps.OrchardCore.Telephony.SoftPhone`, and it is categorized as Telephony. It depends on `CrestApps.OrchardCore.Telephony`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: "Telephony"
    dependencies:
      - CrestApps.OrchardCore.Telephony
---
Provides a provider-agnostic soft phone and SignalR hub for integrating telephony providers.

## Features

### Telephony

Provides the provider-agnostic telephony services, SignalR hub, and site settings. Its manifest-backed feature ID is `CrestApps.OrchardCore.Telephony`, and it is categorized as Telephony. It depends on `OrchardCore.Users`, and `CrestApps.OrchardCore.SignalR`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Telephony Administration

Adds the telephony provider settings screen and its administration menu entry. Its manifest-backed feature ID is `CrestApps.OrchardCore.Telephony.Admin`, and it is categorized as Telephony. It depends on `CrestApps.OrchardCore.Telephony`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Telephony Soft Phone

Injects the floating soft phone experience into the admin dashboard, front end, or both. Its manifest-backed feature ID is `CrestApps.OrchardCore.Telephony.SoftPhone`, and it is categorized as Telephony. It depends on `CrestApps.OrchardCore.Telephony`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

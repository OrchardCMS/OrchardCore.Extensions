---
title: "Omnichannel Management"
slug: CrestApps.OrchardCore.Omnichannel.Managements
description: "Provides the Omnichannel Management module for Orchard Core."
projectUrl: https://github.com/CrestApps/CrestApps.OrchardCore/tree/main/src/Modules/CrestApps.OrchardCore.Omnichannel.Managements
documentationUrl: https://orchardcore.crestapps.com/docs/omnichannel/management
nuGetPackageId: CrestApps.OrchardCore.Omnichannel.Managements
tags: ["CrestApps", "Contact Center"]
author:
  name: The CrestApps Team
  url: https://www.crestapps.com
  imageUrl: https://avatars.githubusercontent.com/u/181091452
licenses: [MIT]
pubDatetime: 2026-08-12T12:00:00Z
features:
  - id: CrestApps.OrchardCore.Omnichannel.Activities
    name: "Omnichannel Activities"
    description: "Adds the headless omnichannel contact, campaign, activity, disposition, subject-flow, and channel-endpoint services, permissions, and storage without any administration screens. Its manifest-backed feature ID is `CrestApps.OrchardCore.Omnichannel.Activities`, and it is categorized as Contact Center. It depends on `CrestApps.OrchardCore.Omnichannel`, `CrestApps.OrchardCore.Users`, `CrestApps.OrchardCore.ContentFields`, `CrestApps.OrchardCore.PhoneNumbers`, `OrchardCore.Contents`, `OrchardCore.Flows`, `OrchardCore.Users`, `CrestApps.OrchardCore.TimeZones`, and `CrestApps.OrchardCore.Users`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: "Contact Center"
    dependencies:
      - CrestApps.OrchardCore.Omnichannel
      - CrestApps.OrchardCore.Users
      - CrestApps.OrchardCore.ContentFields
      - CrestApps.OrchardCore.PhoneNumbers
      - OrchardCore.Contents
      - OrchardCore.Flows
      - OrchardCore.Users
      - CrestApps.OrchardCore.TimeZones
      - CrestApps.OrchardCore.Users
  - id: CrestApps.OrchardCore.Omnichannel.Managements
    name: "Omnichannel Management"
    description: "Adds the omnichannel contact, campaign, activity, disposition, subject-flow, and channel-endpoint administration screens. Its manifest-backed feature ID is `CrestApps.OrchardCore.Omnichannel.Managements`, and it is categorized as Contact Center. It depends on `CrestApps.OrchardCore.Omnichannel.Activities`, `CrestApps.OrchardCore.Resources`, and `OrchardCore.ContentTypes`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: "Contact Center"
    dependencies:
      - CrestApps.OrchardCore.Omnichannel.Activities
      - CrestApps.OrchardCore.Resources
      - OrchardCore.ContentTypes
---
Provides the Omnichannel Management module for Orchard Core.

## Features

### Omnichannel Activities

Adds the headless omnichannel contact, campaign, activity, disposition, subject-flow, and channel-endpoint services, permissions, and storage without any administration screens. Its manifest-backed feature ID is `CrestApps.OrchardCore.Omnichannel.Activities`, and it is categorized as Contact Center. It depends on `CrestApps.OrchardCore.Omnichannel`, `CrestApps.OrchardCore.Users`, `CrestApps.OrchardCore.ContentFields`, `CrestApps.OrchardCore.PhoneNumbers`, `OrchardCore.Contents`, `OrchardCore.Flows`, `OrchardCore.Users`, `CrestApps.OrchardCore.TimeZones`, and `CrestApps.OrchardCore.Users`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Omnichannel Management

Adds the omnichannel contact, campaign, activity, disposition, subject-flow, and channel-endpoint administration screens. Its manifest-backed feature ID is `CrestApps.OrchardCore.Omnichannel.Managements`, and it is categorized as Contact Center. It depends on `CrestApps.OrchardCore.Omnichannel.Activities`, `CrestApps.OrchardCore.Resources`, and `OrchardCore.ContentTypes`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

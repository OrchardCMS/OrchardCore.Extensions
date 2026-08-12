---
title: "Omnichannel"
slug: CrestApps.OrchardCore.Omnichannel
description:
  Provides the Omnichannel module for Orchard Core. It includes Omnichannel and Omnichannel - Azure
  Communication Services features in the Contact Center area, making the package easier to find when browsing
  related Orchard Core capabilities, dependencies, and documentation.
projectUrl: https://github.com/CrestApps/CrestApps.OrchardCore/tree/main/src/Modules/CrestApps.OrchardCore.Omnichannel
documentationUrl: https://orchardcore.crestapps.com/docs/omnichannel/
nuGetPackageId: CrestApps.OrchardCore.Omnichannel
tags: ["crestapps", "Contact Center"]
author:
  name: CrestApps
  url: https://crestapps.com
  imageUrl: https://avatars.githubusercontent.com/u/111536479?s=400&u=d9bdde0365d02b3ed9184034accb696cb12863c5&v=4
licenses: [MIT]
pubDatetime: 2026-08-12T12:00:00Z
features:
  - id: CrestApps.OrchardCore.Omnichannel
    name: "Omnichannel"
    description: "Provides shared omnichannel messages, endpoints, preferences, and processing contracts across communication channels. Its manifest-backed feature ID is `CrestApps.OrchardCore.Omnichannel`, and it is categorized as Contact Center. No additional feature dependencies are listed for it in this catalog entry. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: "Contact Center"
  - id: CrestApps.OrchardCore.Omnichannel.AzureCommunicationServices
    name: "Omnichannel - Azure Communication Services"
    description: "Enables Azure Communication Services email and SMS providers for omnichannel communications. Its manifest-backed feature ID is `CrestApps.OrchardCore.Omnichannel.AzureCommunicationServices`, and it is categorized as Contact Center. It depends on `CrestApps.OrchardCore.Omnichannel`, `OrchardCore.Email.Azure`, and `OrchardCore.Sms.Azure`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: "Contact Center"
    dependencies:
      - CrestApps.OrchardCore.Omnichannel
      - OrchardCore.Email.Azure
      - OrchardCore.Sms.Azure
    documentationUrl: https://orchardcore.crestapps.com/docs/omnichannel/azure-communication-services
---
Provides the Omnichannel module for Orchard Core.

## Features

### Omnichannel

Provides shared omnichannel messages, endpoints, preferences, and processing contracts across communication channels. Its manifest-backed feature ID is `CrestApps.OrchardCore.Omnichannel`, and it is categorized as Contact Center. No additional feature dependencies are listed for it in this catalog entry. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Omnichannel - Azure Communication Services

Enables Azure Communication Services email and SMS providers for omnichannel communications. Its manifest-backed feature ID is `CrestApps.OrchardCore.Omnichannel.AzureCommunicationServices`, and it is categorized as Contact Center. It depends on `CrestApps.OrchardCore.Omnichannel`, `OrchardCore.Email.Azure`, and `OrchardCore.Sms.Azure`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

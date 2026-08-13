---
title: SMS
slug: OrchardCore.Sms
description:
  Provides settings and services to send SMS messages. It includes SMS and SMS Notifications features in the
  Communication and Notifications area, making the package easier to find when browsing related Orchard Core
  capabilities, dependencies, and documentation.
projectUrl: https://github.com/OrchardCMS/OrchardCore/tree/main/src/OrchardCore.Modules/OrchardCore.Sms
documentationUrl: https://docs.orchardcore.net
nuGetPackageId: OrchardCore.Sms
tags: ["Orchard Core"]
author:
  name: The Orchard Core Team
  url: https://docs.orchardcore.net
  imageUrl: https://docs.orchardcore.net/en/latest/assets/images/favicon.png
licenses: [BSD-3-Clause]
compatibleWithAllVersions: true
pubDatetime: 2026-08-12T12:00:00Z
features:
  - id: OrchardCore.Sms
    name: SMS
    description: "Provides settings and services to send SMS messages. Its manifest-backed feature ID is `OrchardCore.Sms`, and it is categorized as Communication. No additional feature dependencies are listed for it in this catalog entry. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Communication
  - id: OrchardCore.Notifications.Sms
    name: SMS Notifications
    description: "Provides a way to send SMS notifications to users. Its manifest-backed feature ID is `OrchardCore.Notifications.Sms`, and it is categorized as Notifications. It depends on `OrchardCore.Notifications`, and `OrchardCore.Sms`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Notifications
    dependencies:
      - OrchardCore.Notifications
      - OrchardCore.Sms
---
Provides settings and services to send SMS messages.

## Features

### SMS

Provides settings and services to send SMS messages. Its manifest-backed feature ID is `OrchardCore.Sms`, and it is categorized as Communication. No additional feature dependencies are listed for it in this catalog entry. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### SMS Notifications

Provides a way to send SMS notifications to users. Its manifest-backed feature ID is `OrchardCore.Notifications.Sms`, and it is categorized as Notifications. It depends on `OrchardCore.Notifications`, and `OrchardCore.Sms`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

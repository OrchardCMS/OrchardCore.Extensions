---
title: OrchardCore.Notifications
slug: OrchardCore.Notifications
description:
  Provides a way to notify users.
projectUrl: https://github.com/OrchardCMS/OrchardCore/tree/main/src/OrchardCore.Modules/OrchardCore.Notifications
documentationUrl: https://docs.orchardcore.net/en/latest/reference/modules/Notifications/
nuGetPackageId: OrchardCore.Notifications
tags: ["Orchard Core"]
author:
  name: The Orchard Core Team
  url: https://github.com/OrchardCMS
  imageUrl: https://avatars.githubusercontent.com/u/9933239
licenses: [BSD-3-Clause]
pubDatetime: 2026-08-12T12:00:00Z
features:
  - id: OrchardCore.Notifications
    name: Notifications
    description: "Provides a way to notify users. Its manifest-backed feature ID is `OrchardCore.Notifications`, and it is categorized as Notifications. It depends on `OrchardCore.Liquid`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Notifications
    dependencies:
      - OrchardCore.Liquid
  - id: OrchardCore.Notifications.Email
    name: Email Notifications
    description: "Provides a way to send email notifications to users. Its manifest-backed feature ID is `OrchardCore.Notifications.Email`, and it is categorized as Notifications. It depends on `OrchardCore.Notifications`, and `OrchardCore.Email`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Notifications
    dependencies:
      - OrchardCore.Notifications
      - OrchardCore.Email
---
Provides a way to notify users.

## Features

### Notifications

Provides a way to notify users. Its manifest-backed feature ID is `OrchardCore.Notifications`, and it is categorized as Notifications. It depends on `OrchardCore.Liquid`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Email Notifications

Provides a way to send email notifications to users. Its manifest-backed feature ID is `OrchardCore.Notifications.Email`, and it is categorized as Notifications. It depends on `OrchardCore.Notifications`, and `OrchardCore.Email`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

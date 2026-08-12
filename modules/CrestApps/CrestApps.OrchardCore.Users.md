---
title: "Users Core Components"
slug: CrestApps.OrchardCore.Users
description: "Provides the Users Core Components module for Orchard Core."
projectUrl: https://github.com/CrestApps/CrestApps.OrchardCore/tree/main/src/Modules/CrestApps.OrchardCore.Users
documentationUrl: https://orchardcore.crestapps.com/docs/modules/users
nuGetPackageId: CrestApps.OrchardCore.Users
tags: ["CrestApps", "Users"]
author:
  name: The CrestApps Team
  url: https://www.crestapps.com
  imageUrl: https://avatars.githubusercontent.com/u/181091452
licenses: [MIT]
pubDatetime: 2026-08-12T12:00:00Z
features:
  - id: CrestApps.OrchardCore.Users
    name: "Users Core Components"
    description: "Provides user components core services. Its manifest-backed feature ID is `CrestApps.OrchardCore.Users`, and it is categorized as Users. No additional feature dependencies are listed for it in this catalog entry. The manifest marks it as enabled by dependency only, so it is intended to support other features rather than be selected as a standalone end-user feature. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: "Users"
    enabledByDependencyOnly: true
  - id: CrestApps.OrchardCore.Users.DisplayName
    name: "User Display Name"
    description: "Provides a way to change how the user name is displayed. Its manifest-backed feature ID is `CrestApps.OrchardCore.Users.DisplayName`, and it is categorized as Users. It depends on `OrchardCore.ContentFields`, and `CrestApps.OrchardCore.Users`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: "Users"
    dependencies:
      - OrchardCore.ContentFields
      - CrestApps.OrchardCore.Users
  - id: CrestApps.OrchardCore.Users.Avatars
    name: "User Avatar"
    description: "Provides a way to display an avatar for each user. Its manifest-backed feature ID is `CrestApps.OrchardCore.Users.Avatars`, and it is categorized as Users. It depends on `OrchardCore.Media`, and `CrestApps.OrchardCore.Users`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: "Users"
    dependencies:
      - OrchardCore.Media
      - CrestApps.OrchardCore.Users
---
Provides the Users Core Components module for Orchard Core.

## Features

### Users Core Components

Provides user components core services. Its manifest-backed feature ID is `CrestApps.OrchardCore.Users`, and it is categorized as Users. No additional feature dependencies are listed for it in this catalog entry. The manifest marks it as enabled by dependency only, so it is intended to support other features rather than be selected as a standalone end-user feature. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### User Display Name

Provides a way to change how the user name is displayed. Its manifest-backed feature ID is `CrestApps.OrchardCore.Users.DisplayName`, and it is categorized as Users. It depends on `OrchardCore.ContentFields`, and `CrestApps.OrchardCore.Users`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### User Avatar

Provides a way to display an avatar for each user. Its manifest-backed feature ID is `CrestApps.OrchardCore.Users.Avatars`, and it is categorized as Users. It depends on `OrchardCore.Media`, and `CrestApps.OrchardCore.Users`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

---
title: Roles
slug: OrchardCore.Roles
description:
  Provides permissions to assign roles to users. Additionally, it updates default roles with default permissions
  provided by features. It includes Roles and Roles Core Services features in the Security area, making the
  package easier to find when browsing related Orchard Core capabilities, dependencies, and documentation.
projectUrl: https://github.com/OrchardCMS/OrchardCore/tree/main/src/OrchardCore.Modules/OrchardCore.Roles
documentationUrl: https://docs.orchardcore.net
nuGetPackageId: OrchardCore.Roles
tags: ["Orchard Core", "Security"]
author:
  name: The Orchard Core Team
  url: https://docs.orchardcore.net
  imageUrl: https://docs.orchardcore.net/en/latest/assets/images/favicon.png
licenses: [BSD-3-Clause]
compatibleWithAllVersions: true
pubDatetime: 2026-08-12T12:00:00Z
features:
  - id: OrchardCore.Roles
    name: Roles
    description: "Provides permissions to assign roles to users. Additionally, it updates default roles with default permissions provided by features. Its manifest-backed feature ID is `OrchardCore.Roles`, and it is categorized as Security. It depends on `OrchardCore.Roles.Core`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Security
    dependencies:
      - OrchardCore.Roles.Core
  - id: OrchardCore.Roles.Core
    name: Roles Core Services
    description: "Provides role core services. Its manifest-backed feature ID is `OrchardCore.Roles.Core`, and it is categorized as Security. No additional feature dependencies are listed for it in this catalog entry. The manifest marks it as enabled by dependency only, so it is intended to support other features rather than be selected as a standalone end-user feature. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Security
    enabledByDependencyOnly: true
---
Provides permissions to assign roles to users. Additionally, it updates default roles with default permissions provided by features.

## Features

### Roles

Provides permissions to assign roles to users. Additionally, it updates default roles with default permissions provided by features. Its manifest-backed feature ID is `OrchardCore.Roles`, and it is categorized as Security. It depends on `OrchardCore.Roles.Core`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Roles Core Services

Provides role core services. Its manifest-backed feature ID is `OrchardCore.Roles.Core`, and it is categorized as Security. No additional feature dependencies are listed for it in this catalog entry. The manifest marks it as enabled by dependency only, so it is intended to support other features rather than be selected as a standalone end-user feature. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

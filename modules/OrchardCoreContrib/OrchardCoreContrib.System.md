---
title: "System"
slug: OrchardCoreContrib.System
description:
  The System module provides information about the currently running application. It helps Orchard Core sites
  add this community-maintained capability while exposing package, dependency, source, and documentation details
  in the extensions gallery.
projectUrl: https://github.com/OrchardCoreContrib/OrchardCoreContrib.Modules/blob/main/src/OrchardCoreContrib.System/README.md
documentationUrl: https://github.com/OrchardCoreContrib/OrchardCoreContrib.Modules/blob/main/src/OrchardCoreContrib.System/README.md
nuGetPackageId: OrchardCoreContrib.System
tags: ["Orchard Core", "System"]
author:
  name: OrchardCoreContrib
  url: https://github.com/OrchardCoreContrib
  imageUrl: https://avatars.githubusercontent.com/u/65380704
licenses: [BSD-3-Clause]
versions:
  - 1.x
  - 2.x
pubDatetime: 2026-07-17T18:28:09Z
features:
  - id: OrchardCoreContrib.System
    name: "System"
    description: "Provides an information about currently running application. Its upstream feature ID is `OrchardCoreContrib.System`, and it is categorized as System. No additional feature dependencies are listed for it in the upstream manifest. This description is based on the OrchardCoreContrib manifest metadata; Orchard Core displays feature entries in the feature management UI with their description, category, and dependencies."
    category: "System"
  - id: OrchardCoreContrib.System.Updates
    name: "System Updates"
    description: "Displays the available system updates. Its upstream feature ID is `OrchardCoreContrib.System.Updates`, and it is categorized as System. It depends on `OrchardCoreContrib.System`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the OrchardCoreContrib manifest metadata; Orchard Core displays feature entries in the feature management UI with their description, category, and dependencies."
    category: "System"
    dependencies:
      - OrchardCoreContrib.System
  - id: OrchardCoreContrib.System.Maintenance
    name: "System Maintenance"
    description: "Put your site in maintenance mode while you're doing upgrades. Its upstream feature ID is `OrchardCoreContrib.System.Maintenance`, and it is categorized as System. It depends on `OrchardCore.Autoroute`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the OrchardCoreContrib manifest metadata; Orchard Core displays feature entries in the feature management UI with their description, category, and dependencies."
    category: "System"
    dependencies:
      - OrchardCore.Autoroute
---
The System module provides information about the currently running application.

## Features

### System

Provides an information about currently running application. Its upstream feature ID is `OrchardCoreContrib.System`, and it is categorized as System. No additional feature dependencies are listed for it in the upstream manifest. This description is based on the OrchardCoreContrib manifest metadata; Orchard Core displays feature entries in the feature management UI with their description, category, and dependencies.

### System Updates

Displays the available system updates. Its upstream feature ID is `OrchardCoreContrib.System.Updates`, and it is categorized as System. It depends on `OrchardCoreContrib.System`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the OrchardCoreContrib manifest metadata; Orchard Core displays feature entries in the feature management UI with their description, category, and dependencies.

### System Maintenance

Put your site in maintenance mode while you're doing upgrades. Its upstream feature ID is `OrchardCoreContrib.System.Maintenance`, and it is categorized as System. It depends on `OrchardCore.Autoroute`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the OrchardCoreContrib manifest metadata; Orchard Core displays feature entries in the feature management UI with their description, category, and dependencies.

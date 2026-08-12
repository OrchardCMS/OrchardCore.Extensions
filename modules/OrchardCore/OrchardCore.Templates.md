---
title: Templates
slug: OrchardCore.Templates
description:
  The Templates module provides a way to write custom shape templates from the admin. It includes Templates and
  Admin Templates features in the Development area, making the package easier to find when browsing related
  Orchard Core capabilities, dependencies, and documentation.
projectUrl: https://github.com/OrchardCMS/OrchardCore/tree/main/src/OrchardCore.Modules/OrchardCore.Templates
documentationUrl: https://docs.orchardcore.net
nuGetPackageId: OrchardCore.Templates
tags: ["Orchard Core"]
author:
  name: The Orchard Core Team
  url: https://docs.orchardcore.net
  imageUrl: https://docs.orchardcore.net/en/latest/assets/images/favicon.png
licenses: [BSD-3-Clause]
pubDatetime: 2026-08-12T12:00:00Z
features:
  - id: OrchardCore.Templates
    name: Templates
    description: "The Templates module provides a way to write custom shape templates from the admin. Its manifest-backed feature ID is `OrchardCore.Templates`, and it is categorized as Development. It depends on `OrchardCore.Liquid`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Development
    dependencies:
      - OrchardCore.Liquid
  - id: OrchardCore.AdminTemplates
    name: Admin Templates
    description: "The Admin Templates module provides a way to write custom admin shape templates. Its manifest-backed feature ID is `OrchardCore.AdminTemplates`, and it is categorized as Development. It depends on `OrchardCore.Templates`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Development
    dependencies:
      - OrchardCore.Templates
---
The Templates module provides a way to write custom shape templates from the admin.

## Features

### Templates

The Templates module provides a way to write custom shape templates from the admin. Its manifest-backed feature ID is `OrchardCore.Templates`, and it is categorized as Development. It depends on `OrchardCore.Liquid`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Admin Templates

The Admin Templates module provides a way to write custom admin shape templates. Its manifest-backed feature ID is `OrchardCore.AdminTemplates`, and it is categorized as Development. It depends on `OrchardCore.Templates`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

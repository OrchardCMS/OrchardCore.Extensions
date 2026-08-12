---
title: Admin
slug: OrchardCore.Admin
description:
  Creates an admin section for the site. It helps site owners add this capability to Orchard Core sites while
  exposing package, dependency, and documentation details in the extensions gallery.
projectUrl: https://github.com/OrchardCMS/OrchardCore/tree/main/src/OrchardCore.Modules/OrchardCore.Admin
documentationUrl: https://docs.orchardcore.net
nuGetPackageId: OrchardCore.Admin
tags: ["Orchard Core", "Infrastructure"]
author:
  name: The Orchard Core Team
  url: https://docs.orchardcore.net
  imageUrl: https://docs.orchardcore.net/en/latest/assets/images/favicon.png
licenses: [BSD-3-Clause]
dependencies: ["OrchardCore.Settings"]
pubDatetime: 2026-08-12T12:00:00Z
features:
  - id: OrchardCore.Admin
    name: Admin
    description: "Creates an admin section for the site. Its manifest-backed feature ID is `OrchardCore.Admin`, and it is categorized as Infrastructure. It depends on `OrchardCore.Settings`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Infrastructure
    dependencies:
      - OrchardCore.Settings
---
Creates an admin section for the site.

## Features

### Admin

Creates an admin section for the site. Its manifest-backed feature ID is `OrchardCore.Admin`, and it is categorized as Infrastructure. It depends on `OrchardCore.Settings`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

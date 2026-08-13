---
title: "Reports"
slug: CrestApps.OrchardCore.Reports
description:
  Provides a reusable reporting framework with a shared admin Reports area, extensible filters, and exports. It
  helps site owners add this capability to Orchard Core sites while exposing package, dependency, and
  documentation details in the extensions gallery.
projectUrl: https://github.com/CrestApps/CrestApps.OrchardCore/tree/main/src/Modules/CrestApps.OrchardCore.Reports
documentationUrl: https://orchardcore.crestapps.com
nuGetPackageId: CrestApps.OrchardCore.Reports
tags: ["crestapps", "Reporting"]
author:
  name: CrestApps
  url: https://crestapps.com
  imageUrl: https://avatars.githubusercontent.com/u/111536479
licenses: [MIT]
versions:
  - 2.x
  - 3.x
pubDatetime: 2026-08-12T12:00:00Z
features:
  - id: CrestApps.OrchardCore.Reports
    name: "Reports"
    description: "Adds the admin Reports area, the extensible report filter with a from/to date range, the uniform report renderer, and CSV export. Other modules contribute reports to this area. Its manifest-backed feature ID is `CrestApps.OrchardCore.Reports`, and it is categorized as Reporting. It depends on `CrestApps.OrchardCore.Resources`, and `OrchardCore.Users`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: "Reporting"
    dependencies:
      - CrestApps.OrchardCore.Resources
      - OrchardCore.Users
---
Provides a reusable reporting framework with a shared admin Reports area, extensible filters, and exports.

## Features

### Reports

Adds the admin Reports area, the extensible report filter with a from/to date range, the uniform report renderer, and CSV export. Other modules contribute reports to this area. Its manifest-backed feature ID is `CrestApps.OrchardCore.Reports`, and it is categorized as Reporting. It depends on `CrestApps.OrchardCore.Resources`, and `OrchardCore.Users`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

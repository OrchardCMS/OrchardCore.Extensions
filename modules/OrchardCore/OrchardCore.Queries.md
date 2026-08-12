---
title: Queries
slug: OrchardCore.Queries
description:
  Provides querying capability services. It includes Queries Core Services, Queries and SQL Queries features in
  the Content Management area, making the package easier to find when browsing related Orchard Core
  capabilities, dependencies, and documentation.
projectUrl: https://github.com/OrchardCMS/OrchardCore/tree/main/src/OrchardCore.Modules/OrchardCore.Queries
documentationUrl: https://docs.orchardcore.net/en/latest/reference/modules/Queries/
nuGetPackageId: OrchardCore.Queries
tags: ["Orchard Core"]
author:
  name: The Orchard Core Team
  url: https://docs.orchardcore.net
  imageUrl: https://docs.orchardcore.net/en/latest/assets/images/favicon.png
licenses: [BSD-3-Clause]
pubDatetime: 2026-08-12T12:00:00Z
features:
  - id: OrchardCore.Queries.Core
    name: Queries Core Services
    description: "Provides querying capability services. Its manifest-backed feature ID is `OrchardCore.Queries.Core`, and it is categorized as Content Management. It depends on `OrchardCore.Liquid`, so Orchard Core enables that dependency when this feature is enabled. The manifest marks it as enabled by dependency only, so it is intended to support other features rather than be selected as a standalone end-user feature. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Content Management
    dependencies:
      - OrchardCore.Liquid
    enabledByDependencyOnly: true
  - id: OrchardCore.Queries
    name: Queries
    description: "Provides querying capabilities. Its manifest-backed feature ID is `OrchardCore.Queries`, and it is categorized as Content Management. It depends on `OrchardCore.Queries.Core`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Content Management
    dependencies:
      - OrchardCore.Queries.Core
  - id: OrchardCore.Queries.Sql
    name: SQL Queries
    description: "Introduces a way to create custom Queries in pure SQL. Its manifest-backed feature ID is `OrchardCore.Queries.Sql`, and it is categorized as Content Management. It depends on `OrchardCore.Queries`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Content Management
    dependencies:
      - OrchardCore.Queries
---
Provides querying capability services.

## Features

### Queries Core Services

Provides querying capability services. Its manifest-backed feature ID is `OrchardCore.Queries.Core`, and it is categorized as Content Management. It depends on `OrchardCore.Liquid`, so Orchard Core enables that dependency when this feature is enabled. The manifest marks it as enabled by dependency only, so it is intended to support other features rather than be selected as a standalone end-user feature. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Queries

Provides querying capabilities. Its manifest-backed feature ID is `OrchardCore.Queries`, and it is categorized as Content Management. It depends on `OrchardCore.Queries.Core`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### SQL Queries

Introduces a way to create custom Queries in pure SQL. Its manifest-backed feature ID is `OrchardCore.Queries.Sql`, and it is categorized as Content Management. It depends on `OrchardCore.Queries`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

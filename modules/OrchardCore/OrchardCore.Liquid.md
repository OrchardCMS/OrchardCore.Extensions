---
title: Liquid
slug: OrchardCore.Liquid
description:
  The liquid module enables content items to have liquid syntax. It includes Liquid and Liquid Core Services
  features in the Content Management area, making the package easier to find when browsing related Orchard Core
  capabilities, dependencies, and documentation.
projectUrl: https://github.com/OrchardCMS/OrchardCore/tree/main/src/OrchardCore.Modules/OrchardCore.Liquid
documentationUrl: https://docs.orchardcore.net/en/latest/reference/modules/Liquid/
nuGetPackageId: OrchardCore.Liquid
tags: ["Orchard Core", "Content Management"]
author:
  name: The Orchard Core Team
  url: https://docs.orchardcore.net
  imageUrl: https://docs.orchardcore.net/en/latest/assets/images/orchard-logo.png
licenses: [BSD-3-Clause]
pubDatetime: 2026-08-12T12:00:00Z
features:
  - id: OrchardCore.Liquid
    name: Liquid
    description: "The liquid module enables content items to have liquid syntax. Its manifest-backed feature ID is `OrchardCore.Liquid`, and it is categorized as Content Management. It depends on `OrchardCore.Liquid.Core`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Content Management
    dependencies:
      - OrchardCore.Liquid.Core
  - id: OrchardCore.Liquid.Core
    name: Liquid Core Services
    description: "Provides liquid core services. Its manifest-backed feature ID is `OrchardCore.Liquid.Core`, and it is categorized as Content Management. No additional feature dependencies are listed for it in this catalog entry. The manifest marks it as enabled by dependency only, so it is intended to support other features rather than be selected as a standalone end-user feature. The manifest marks it as always enabled, so administrators cannot turn it off from the feature management screen. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Content Management
    enabledByDependencyOnly: true
    alwaysEnabled: true
---
The liquid module enables content items to have liquid syntax.

## Features

### Liquid

The liquid module enables content items to have liquid syntax. Its manifest-backed feature ID is `OrchardCore.Liquid`, and it is categorized as Content Management. It depends on `OrchardCore.Liquid.Core`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Liquid Core Services

Provides liquid core services. Its manifest-backed feature ID is `OrchardCore.Liquid.Core`, and it is categorized as Content Management. No additional feature dependencies are listed for it in this catalog entry. The manifest marks it as enabled by dependency only, so it is intended to support other features rather than be selected as a standalone end-user feature. The manifest marks it as always enabled, so administrators cannot turn it off from the feature management screen. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

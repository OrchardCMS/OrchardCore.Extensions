---
title: OrchardCore.Recipes
slug: OrchardCore.Recipes
description:
  The Recipes module allows you to execute recipe steps from json files.
projectUrl: https://github.com/OrchardCMS/OrchardCore/tree/main/src/OrchardCore.Modules/OrchardCore.Recipes
documentationUrl: https://docs.orchardcore.net/en/latest/reference/modules/Recipes/
nuGetPackageId: OrchardCore.Recipes
tags: ["Orchard Core"]
author:
  name: The Orchard Core Team
  url: https://github.com/OrchardCMS
  imageUrl: https://avatars.githubusercontent.com/u/9933239
licenses: [BSD-3-Clause]
pubDatetime: 2026-08-12T12:00:00Z
features:
  - id: OrchardCore.Recipes
    name: Recipes
    description: "The Recipes module allows you to execute recipe steps from json files. Its manifest-backed feature ID is `OrchardCore.Recipes`, and it is categorized as Infrastructure. It depends on `OrchardCore.Recipes.Core`, and `OrchardCore.Scripting`, so Orchard Core enables those dependencies when this feature is enabled. The manifest marks it as always enabled, so administrators cannot turn it off from the feature management screen. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Infrastructure
    dependencies:
      - OrchardCore.Recipes.Core
      - OrchardCore.Scripting
    alwaysEnabled: true
  - id: OrchardCore.Recipes.Core
    name: Recipes Core Services
    description: "Provides recipe core services. Its manifest-backed feature ID is `OrchardCore.Recipes.Core`, and it is categorized as Infrastructure. No additional feature dependencies are listed for it in this catalog entry. The manifest marks it as enabled by dependency only, so it is intended to support other features rather than be selected as a standalone end-user feature. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Infrastructure
    enabledByDependencyOnly: true
---
The Recipes module allows you to execute recipe steps from json files.

## Features

### Recipes

The Recipes module allows you to execute recipe steps from json files. Its manifest-backed feature ID is `OrchardCore.Recipes`, and it is categorized as Infrastructure. It depends on `OrchardCore.Recipes.Core`, and `OrchardCore.Scripting`, so Orchard Core enables those dependencies when this feature is enabled. The manifest marks it as always enabled, so administrators cannot turn it off from the feature management screen. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Recipes Core Services

Provides recipe core services. Its manifest-backed feature ID is `OrchardCore.Recipes.Core`, and it is categorized as Infrastructure. No additional feature dependencies are listed for it in this catalog entry. The manifest marks it as enabled by dependency only, so it is intended to support other features rather than be selected as a standalone end-user feature. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

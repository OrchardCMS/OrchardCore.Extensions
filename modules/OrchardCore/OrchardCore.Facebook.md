---
title: Meta
slug: OrchardCore.Facebook
description:
  Registers the core components used by the Meta features. It includes Meta Core Components, Meta Login and
  related features in the Meta area, making the package easier to find when browsing related Orchard Core
  capabilities, dependencies, and documentation.
projectUrl: https://github.com/OrchardCMS/OrchardCore/tree/main/src/OrchardCore.Modules/OrchardCore.Facebook
documentationUrl: https://docs.orchardcore.net
nuGetPackageId: OrchardCore.Facebook
tags: ["Orchard Core", "Meta"]
author:
  name: The Orchard Core Team
  url: https://docs.orchardcore.net
  imageUrl: https://docs.orchardcore.net/en/latest/assets/images/favicon.png
licenses: [BSD-3-Clause]
pubDatetime: 2026-08-12T12:00:00Z
features:
  - id: OrchardCore.Facebook
    name: Meta Core Components
    description: "Registers the core components used by the Meta features. Its manifest-backed feature ID is `OrchardCore.Facebook`, and it is categorized as Meta. No additional feature dependencies are listed for it in this catalog entry. The manifest marks it as enabled by dependency only, so it is intended to support other features rather than be selected as a standalone end-user feature. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Meta
    enabledByDependencyOnly: true
  - id: OrchardCore.Facebook.Login
    name: Meta Login
    description: "Authenticates users from Meta. Its manifest-backed feature ID is `OrchardCore.Facebook.Login`, and it is categorized as Meta. It depends on `OrchardCore.Facebook`, and `OrchardCore.Users.ExternalAuthentication`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Meta
    dependencies:
      - OrchardCore.Facebook
      - OrchardCore.Users.ExternalAuthentication
  - id: OrchardCore.Facebook.Widgets
    name: Meta Social Plugins Widgets
    description: "Integrates Meta social plugins as predefined widgets. Its manifest-backed feature ID is `OrchardCore.Facebook.Widgets`, and it is categorized as Meta. It depends on `OrchardCore.Facebook`, `OrchardCore.Widgets`, and `OrchardCore.Recipes.Core`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Meta
    dependencies:
      - OrchardCore.Facebook
      - OrchardCore.Widgets
      - OrchardCore.Recipes.Core
  - id: OrchardCore.Facebook.Pixel
    name: Meta Pixel
    description: "Provides a way to enable Meta Pixel tracking for your site. Its manifest-backed feature ID is `OrchardCore.Facebook.Pixel`, and it is categorized as Meta. No additional feature dependencies are listed for it in this catalog entry. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Meta
---
Registers the core components used by the Meta features.

## Features

### Meta Core Components

Registers the core components used by the Meta features. Its manifest-backed feature ID is `OrchardCore.Facebook`, and it is categorized as Meta. No additional feature dependencies are listed for it in this catalog entry. The manifest marks it as enabled by dependency only, so it is intended to support other features rather than be selected as a standalone end-user feature. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Meta Login

Authenticates users from Meta. Its manifest-backed feature ID is `OrchardCore.Facebook.Login`, and it is categorized as Meta. It depends on `OrchardCore.Facebook`, and `OrchardCore.Users.ExternalAuthentication`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Meta Social Plugins Widgets

Integrates Meta social plugins as predefined widgets. Its manifest-backed feature ID is `OrchardCore.Facebook.Widgets`, and it is categorized as Meta. It depends on `OrchardCore.Facebook`, `OrchardCore.Widgets`, and `OrchardCore.Recipes.Core`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Meta Pixel

Provides a way to enable Meta Pixel tracking for your site. Its manifest-backed feature ID is `OrchardCore.Facebook.Pixel`, and it is categorized as Meta. No additional feature dependencies are listed for it in this catalog entry. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

---
title: Features
slug: OrchardCore.Features
description:
  The Features module enables the administrator of the site to manage the installed modules as well as activate
  and de-activate features. It helps site owners add this capability to Orchard Core sites while exposing
  package, dependency, and documentation details in the extensions gallery.
projectUrl: https://github.com/OrchardCMS/OrchardCore/tree/main/src/OrchardCore.Modules/OrchardCore.Features
documentationUrl: https://docs.orchardcore.net
nuGetPackageId: OrchardCore.Features
tags: ["Orchard Core"]
author:
  name: The Orchard Core Team
  url: https://docs.orchardcore.net
  imageUrl: https://docs.orchardcore.net/en/latest/assets/images/favicon.png
licenses: [BSD-3-Clause]
compatibleWithAllVersions: true
pubDatetime: 2026-08-12T12:00:00Z
features:
  - id: OrchardCore.Features
    name: Features
    description: "The Features module enables the administrator of the site to manage the installed modules as well as activate and de-activate features. Its manifest-backed feature ID is `OrchardCore.Features`, and it is categorized as Infrastructure. It depends on `OrchardCore.Resources`, so Orchard Core enables that dependency when this feature is enabled. The manifest marks it as always enabled, so administrators cannot turn it off from the feature management screen. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Infrastructure
    dependencies:
      - OrchardCore.Resources
    alwaysEnabled: true
---
The Features module enables the administrator of the site to manage the installed modules as well as activate and de-activate features.

## Features

### Features

The Features module enables the administrator of the site to manage the installed modules as well as activate and de-activate features. Its manifest-backed feature ID is `OrchardCore.Features`, and it is categorized as Infrastructure. It depends on `OrchardCore.Resources`, so Orchard Core enables that dependency when this feature is enabled. The manifest marks it as always enabled, so administrators cannot turn it off from the feature management screen. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

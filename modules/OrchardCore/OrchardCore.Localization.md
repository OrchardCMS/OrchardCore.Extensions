---
title: Localization
slug: OrchardCore.Localization
description:
  Provides support for UI localization. It includes Localization, Content Language Header and Admin Culture
  Picker features in the Internationalization area, making the package easier to find when browsing related
  Orchard Core capabilities, dependencies, and documentation.
projectUrl: https://github.com/OrchardCMS/OrchardCore/tree/main/src/OrchardCore.Modules/OrchardCore.Localization
documentationUrl: https://docs.orchardcore.net
nuGetPackageId: OrchardCore.Localization
tags: ["Orchard Core"]
author:
  name: The Orchard Core Team
  url: https://docs.orchardcore.net
  imageUrl: https://docs.orchardcore.net/en/latest/assets/images/favicon.png
licenses: [BSD-3-Clause]
compatibleWithAllVersions: true
pubDatetime: 2026-08-12T12:00:00Z
features:
  - id: OrchardCore.Localization
    name: Localization
    description: "Provides support for UI localization. Its manifest-backed feature ID is `OrchardCore.Localization`, and it is categorized as Internationalization. It depends on `OrchardCore.Settings`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Internationalization
    dependencies:
      - OrchardCore.Settings
  - id: OrchardCore.Localization.ContentLanguageHeader
    name: Content Language Header
    description: "Adds the Content-Language HTTP header, which describes the language(s) intended for the audience. Its manifest-backed feature ID is `OrchardCore.Localization.ContentLanguageHeader`, and it is categorized as Internationalization. It depends on `OrchardCore.Localization`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Internationalization
    dependencies:
      - OrchardCore.Localization
  - id: OrchardCore.Localization.AdminCulturePicker
    name: Admin Culture Picker
    description: "Provides a culture picker shape for the admin area. Its manifest-backed feature ID is `OrchardCore.Localization.AdminCulturePicker`, and it is categorized as Internationalization. It depends on `OrchardCore.Localization`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Internationalization
    dependencies:
      - OrchardCore.Localization
---
Provides support for UI localization.

## Features

### Localization

Provides support for UI localization. Its manifest-backed feature ID is `OrchardCore.Localization`, and it is categorized as Internationalization. It depends on `OrchardCore.Settings`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Content Language Header

Adds the Content-Language HTTP header, which describes the language(s) intended for the audience. Its manifest-backed feature ID is `OrchardCore.Localization.ContentLanguageHeader`, and it is categorized as Internationalization. It depends on `OrchardCore.Localization`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Admin Culture Picker

Provides a culture picker shape for the admin area. Its manifest-backed feature ID is `OrchardCore.Localization.AdminCulturePicker`, and it is categorized as Internationalization. It depends on `OrchardCore.Localization`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

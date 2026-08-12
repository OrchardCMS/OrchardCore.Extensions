---
title: Content Localization
slug: OrchardCore.ContentLocalization
description:
  Provides a part that allows to localize content items.
projectUrl: https://github.com/OrchardCMS/OrchardCore/tree/main/src/OrchardCore.Modules/OrchardCore.ContentLocalization
documentationUrl: https://docs.orchardcore.net/en/latest/reference/modules/ContentLocalization/
nuGetPackageId: OrchardCore.ContentLocalization
tags: ["Orchard Core", "Internationalization"]
author:
  name: The Orchard Core Team
  url: https://github.com/OrchardCMS
  imageUrl: https://avatars.githubusercontent.com/u/9933239
licenses: [BSD-3-Clause]
pubDatetime: 2026-08-12T12:00:00Z
features:
  - id: OrchardCore.ContentLocalization
    name: Content Localization
    description: "Provides a part that allows to localize content items. Its manifest-backed feature ID is `OrchardCore.ContentLocalization`, and it is categorized as Internationalization. It depends on `OrchardCore.ContentTypes`, and `OrchardCore.Localization`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Internationalization
    dependencies:
      - OrchardCore.ContentTypes
      - OrchardCore.Localization
  - id: OrchardCore.ContentLocalization.ContentCulturePicker
    name: Content Culture Picker
    description: "Provides a culture picker shape for the frontend. Its manifest-backed feature ID is `OrchardCore.ContentLocalization.ContentCulturePicker`, and it is categorized as Internationalization. It depends on `OrchardCore.ContentLocalization`, and `OrchardCore.Autoroute`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Internationalization
    dependencies:
      - OrchardCore.ContentLocalization
      - OrchardCore.Autoroute
  - id: OrchardCore.ContentLocalization.Sitemaps
    name: Localized Content Item Sitemaps
    description: "Provides support for localized content item sitemaps. Its manifest-backed feature ID is `OrchardCore.ContentLocalization.Sitemaps`, and it is categorized as Internationalization. It depends on `OrchardCore.ContentLocalization`, and `OrchardCore.Sitemaps`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Internationalization
    dependencies:
      - OrchardCore.ContentLocalization
      - OrchardCore.Sitemaps
---
Provides a part that allows to localize content items.

## Features

### Content Localization

Provides a part that allows to localize content items. Its manifest-backed feature ID is `OrchardCore.ContentLocalization`, and it is categorized as Internationalization. It depends on `OrchardCore.ContentTypes`, and `OrchardCore.Localization`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Content Culture Picker

Provides a culture picker shape for the frontend. Its manifest-backed feature ID is `OrchardCore.ContentLocalization.ContentCulturePicker`, and it is categorized as Internationalization. It depends on `OrchardCore.ContentLocalization`, and `OrchardCore.Autoroute`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Localized Content Item Sitemaps

Provides support for localized content item sitemaps. Its manifest-backed feature ID is `OrchardCore.ContentLocalization.Sitemaps`, and it is categorized as Internationalization. It depends on `OrchardCore.ContentLocalization`, and `OrchardCore.Sitemaps`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

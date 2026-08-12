---
title: "Orchard Core Contrib - Content Localization"
slug: OrchardCoreContrib.ContentLocalization
description:
  Provides a list of content localization features such as localization matrix. It helps Orchard Core sites add
  this community-maintained capability while exposing package, dependency, source, and documentation details in
  the extensions gallery.
projectUrl: https://github.com/OrchardCoreContrib/OrchardCoreContrib.Modules/blob/main/src/OrchardCoreContrib.ContentLocalization/README.md
documentationUrl: https://github.com/OrchardCoreContrib/OrchardCoreContrib.Modules/blob/main/src/OrchardCoreContrib.ContentLocalization/README.md
nuGetPackageId: OrchardCoreContrib.ContentLocalization
tags: ["Orchard Core", "Content Localization"]
author:
  name: OrchardCoreContrib
  url: https://github.com/OrchardCoreContrib
  imageUrl: https://avatars.githubusercontent.com/u/65380704
licenses: [BSD-3-Clause]
pubDatetime: 2026-07-17T18:28:09Z
features:
  - id: OrchardCoreContrib.ContentLocalization.LocalizationMatrix
    name: "Localization Matrix"
    description: "Provides a matrix shows the localized content per culture. Its upstream feature ID is `OrchardCoreContrib.ContentLocalization.LocalizationMatrix`, and it is categorized as Internationalization. It depends on `OrchardCore.ContentLocalization`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the OrchardCoreContrib manifest metadata; Orchard Core displays feature entries in the feature management UI with their description, category, and dependencies."
    category: "Internationalization"
    dependencies:
      - OrchardCore.ContentLocalization
  - id: OrchardCoreContrib.ContentLocalization.Transliteration
    name: "Transliteration"
    description: "Provides a type of conversion of a text from one script to another that involves swapping letters. Its upstream feature ID is `OrchardCoreContrib.ContentLocalization.Transliteration`, and it is categorized as Internationalization. No additional feature dependencies are listed for it in the upstream manifest. This description is based on the OrchardCoreContrib manifest metadata; Orchard Core displays feature entries in the feature management UI with their description, category, and dependencies."
    category: "Internationalization"
---
Provides a list of content localization features such as localization matrix.

## Features

### Localization Matrix

Provides a matrix shows the localized content per culture. Its upstream feature ID is `OrchardCoreContrib.ContentLocalization.LocalizationMatrix`, and it is categorized as Internationalization. It depends on `OrchardCore.ContentLocalization`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the OrchardCoreContrib manifest metadata; Orchard Core displays feature entries in the feature management UI with their description, category, and dependencies.

### Transliteration

Provides a type of conversion of a text from one script to another that involves swapping letters. Its upstream feature ID is `OrchardCoreContrib.ContentLocalization.Transliteration`, and it is categorized as Internationalization. No additional feature dependencies are listed for it in the upstream manifest. This description is based on the OrchardCoreContrib manifest metadata; Orchard Core displays feature entries in the feature management UI with their description, category, and dependencies.

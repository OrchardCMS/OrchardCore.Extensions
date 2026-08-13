---
title: "Orchard Core Commerce - Content Fields"
slug: OrchardCore.Commerce.ContentFields
description:
  Commerce-specific content fields. It helps Orchard Core sites add commerce capabilities while exposing
  package, dependency, source, and documentation details in the extensions gallery.
projectUrl: https://github.com/OrchardCMS/OrchardCore.Commerce/tree/main/src/Modules/OrchardCore.Commerce.ContentFields
documentationUrl: https://docs.orchardcore.net
nuGetPackageId: OrchardCore.Commerce.ContentFields
tags: ["Orchard Core", "Commerce", "e-Commerce", "ContentFields"]
author:
  name: The Orchard Core Team
  url: https://docs.orchardcore.net
  imageUrl: https://docs.orchardcore.net/en/latest/assets/images/favicon.png
licenses: [BSD-3-Clause]
compatibleWithAllVersions: true
pubDatetime: 2026-07-30T23:08:43Z
features:
  - id: OrchardCore.Commerce.ContentFields
    name: "Orchard Core Commerce - Content Fields"
    description: "Commerce-specific content fields for Orchard Core. Its upstream feature ID is `OrchardCore.Commerce.ContentFields`, and it is categorized as Commerce. It depends on `OrchardCore.ContentFields`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core Commerce manifest metadata; Orchard Core displays feature entries in the feature management UI with their description, category, and dependencies."
    category: Commerce
    dependencies:
      - OrchardCore.ContentFields
  - id: OrchardCore.Commerce.ContentFields.WesternNameParts
    name: "Orchard Core Commerce - Western Name Parts"
    description: "Enabling this feature provides an address updater and shape override for the address editor that implements common name parts in English-speaking and many other western cultures. This will break up the Name field into Title, Given Name, Middle Name and Family Name fields. Its upstream feature ID is `OrchardCore.Commerce.ContentFields.WesternNameParts`, and it is categorized as Commerce. It depends on `OrchardCore.Commerce.ContentFields`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core Commerce manifest metadata; Orchard Core displays feature entries in the feature management UI with their description, category, and dependencies."
    category: Commerce
    dependencies:
      - OrchardCore.Commerce.ContentFields
---
Commerce-specific content fields.

## Features

### Orchard Core Commerce - Content Fields

Commerce-specific content fields for Orchard Core. Its upstream feature ID is `OrchardCore.Commerce.ContentFields`, and it is categorized as Commerce. It depends on `OrchardCore.ContentFields`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core Commerce manifest metadata; Orchard Core displays feature entries in the feature management UI with their description, category, and dependencies.

### Orchard Core Commerce - Western Name Parts

Enabling this feature provides an address updater and shape override for the address editor that implements common name parts in English-speaking and many other western cultures. This will break up the Name field into Title, Given Name, Middle Name and Family Name fields. Its upstream feature ID is `OrchardCore.Commerce.ContentFields.WesternNameParts`, and it is categorized as Commerce. It depends on `OrchardCore.Commerce.ContentFields`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core Commerce manifest metadata; Orchard Core displays feature entries in the feature management UI with their description, category, and dependencies.

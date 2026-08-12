---
title: "Orchard Core Commerce - Payment"
slug: OrchardCore.Commerce.Payment
description:
  Payment for Orchard Core Commerce. It helps Orchard Core sites add commerce capabilities while exposing
  package, dependency, source, and documentation details in the extensions gallery.
projectUrl: https://github.com/OrchardCMS/OrchardCore.Commerce/tree/main/src/Modules/OrchardCore.Commerce.Payment
documentationUrl: https://docs.orchardcore.net
nuGetPackageId: OrchardCore.Commerce.Payment
tags: ["Orchard Core", "Commerce", "e-Commerce", "Payment"]
author:
  name: The Orchard Core Team
  url: https://docs.orchardcore.net
  imageUrl: https://docs.orchardcore.net/en/latest/assets/images/favicon.png
licenses: [BSD-3-Clause]
pubDatetime: 2026-07-30T23:08:43Z
features:
  - id: OrchardCore.Commerce.Payment
    name: "Orchard Core Commerce - Payment"
    description: "Payment for Orchard Core Commerce. Its upstream feature ID is `OrchardCore.Commerce.Payment`, and it is categorized as Commerce. It depends on `OrchardCore.Commerce.ContentFields`, and `OrchardCore.Commerce.Tax`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core Commerce manifest metadata; Orchard Core displays feature entries in the feature management UI with their description, category, and dependencies."
    category: Commerce
    dependencies:
      - OrchardCore.Commerce.ContentFields
      - OrchardCore.Commerce.Tax
  - id: OrchardCore.Commerce.Payment.DummyProvider
    name: "Orchard Core Commerce - Payment - Dummy Provider"
    description: "Dummy payment provider used for development and testing. Its upstream feature ID is `OrchardCore.Commerce.Payment.DummyProvider`, and it is categorized as Commerce. It depends on `OrchardCore.Commerce.Payment`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core Commerce manifest metadata; Orchard Core displays feature entries in the feature management UI with their description, category, and dependencies."
    category: Commerce
    dependencies:
      - OrchardCore.Commerce.Payment
---
Payment for Orchard Core Commerce.

## Features

### Orchard Core Commerce - Payment

Payment for Orchard Core Commerce. Its upstream feature ID is `OrchardCore.Commerce.Payment`, and it is categorized as Commerce. It depends on `OrchardCore.Commerce.ContentFields`, and `OrchardCore.Commerce.Tax`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core Commerce manifest metadata; Orchard Core displays feature entries in the feature management UI with their description, category, and dependencies.

### Orchard Core Commerce - Payment - Dummy Provider

Dummy payment provider used for development and testing. Its upstream feature ID is `OrchardCore.Commerce.Payment.DummyProvider`, and it is categorized as Commerce. It depends on `OrchardCore.Commerce.Payment`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core Commerce manifest metadata; Orchard Core displays feature entries in the feature management UI with their description, category, and dependencies.

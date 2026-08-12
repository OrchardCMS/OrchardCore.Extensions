---
title: "Orchard Core Commerce - Tax"
slug: OrchardCore.Commerce.Tax
description:
  Taxation module for Orchard Core Commerce for sales tax or VAT. It helps Orchard Core sites add commerce
  capabilities while exposing package, dependency, source, and documentation details in the extensions gallery.
projectUrl: https://github.com/OrchardCMS/OrchardCore.Commerce/tree/main/src/Modules/OrchardCore.Commerce.Tax
documentationUrl: https://github.com/OrchardCMS/OrchardCore.Commerce/tree/main/src/Modules/OrchardCore.Commerce.Tax
nuGetPackageId: OrchardCore.Commerce.Tax
tags: ["Orchard Core", "Commerce", "e-Commerce", "Tax", "Sales Tax", "VAT"]
author:
  name: The Orchard Core Team
  url: https://docs.orchardcore.net
  imageUrl: https://docs.orchardcore.net/en/latest/assets/images/favicon.png
licenses: [BSD-3-Clause]
pubDatetime: 2026-07-30T23:08:43Z
features:
  - id: OrchardCore.Commerce.Tax
    name: "Orchard Core Commerce - Tax"
    description: "Core tax features for Orchard Core Commerce. Its upstream feature ID is `OrchardCore.Commerce.Tax`, and it is categorized as Commerce. No additional feature dependencies are listed for it in the upstream manifest. This description is based on the Orchard Core Commerce manifest metadata; Orchard Core displays feature entries in the feature management UI with their description, category, and dependencies."
    category: Commerce
  - id: OrchardCore.Commerce.Tax.CustomTaxRates
    name: "Orchard Core Commerce - Custom Tax Rates"
    description: "Enables administrators to locally maintain a set of tax rates. Its upstream feature ID is `OrchardCore.Commerce.Tax.CustomTaxRates`, and it is categorized as Commerce. It depends on `OrchardCore.Commerce.Tax`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core Commerce manifest metadata; Orchard Core displays feature entries in the feature management UI with their description, category, and dependencies."
    category: Commerce
    dependencies:
      - OrchardCore.Commerce.Tax
---
Taxation module for Orchard Core Commerce for sales tax or VAT.

## Features

### Orchard Core Commerce - Tax

Core tax features for Orchard Core Commerce. Its upstream feature ID is `OrchardCore.Commerce.Tax`, and it is categorized as Commerce. No additional feature dependencies are listed for it in the upstream manifest. This description is based on the Orchard Core Commerce manifest metadata; Orchard Core displays feature entries in the feature management UI with their description, category, and dependencies.

### Orchard Core Commerce - Custom Tax Rates

Enables administrators to locally maintain a set of tax rates. Its upstream feature ID is `OrchardCore.Commerce.Tax.CustomTaxRates`, and it is categorized as Commerce. It depends on `OrchardCore.Commerce.Tax`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core Commerce manifest metadata; Orchard Core displays feature entries in the feature management UI with their description, category, and dependencies.

---
title: E-commerce
slug: OrchardCore.Commerce
description:
  The commerce module for Orchard Core. It helps Orchard Core sites add commerce capabilities while exposing
  package, dependency, source, and documentation details in the extensions gallery.
projectUrl: https://github.com/OrchardCMS/OrchardCore.Commerce/tree/main/src/Modules/OrchardCore.Commerce
documentationUrl: https://docs.orchardcore.net
nuGetPackageId: OrchardCore.Commerce
tags: ["Orchard Core", "Commerce", "e-Commerce"]
author:
  name: The Orchard Core Team
  url: https://docs.orchardcore.net
  imageUrl: https://docs.orchardcore.net/en/latest/assets/images/favicon.png
licenses: [BSD-3-Clause]
compatibleWithAllVersions: true
pubDatetime: 2026-07-30T23:08:43Z
features:
  - id: OrchardCore.Commerce
    name: "Orchard Core Commerce - Core"
    description: "Registers the core components used by the Commerce features. Its upstream feature ID is `OrchardCore.Commerce`, and it is categorized as Commerce. It depends on `OrchardCore.Contents`, `OrchardCore.Workflows`, `OrchardCore.Templates`, `OrchardCore.Commerce.ContentFields`, and `OrchardCore.Commerce.Payment`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core Commerce manifest metadata; Orchard Core displays feature entries in the feature management UI with their description, category, and dependencies."
    category: Commerce
    dependencies:
      - OrchardCore.Contents
      - OrchardCore.Workflows
      - OrchardCore.Templates
      - OrchardCore.Commerce.ContentFields
      - OrchardCore.Commerce.Payment
  - id: OrchardCore.Commerce.SessionCartStorage
    name: "Orchard Core Commerce - Session Cart Storage"
    description: "Registers session-based shopping cart persistence. Its upstream feature ID is `OrchardCore.Commerce.SessionCartStorage`, and it is categorized as Commerce. It depends on `OrchardCore.Contents`, and `OrchardCore.Commerce`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core Commerce manifest metadata; Orchard Core displays feature entries in the feature management UI with their description, category, and dependencies."
    category: Commerce
    dependencies:
      - OrchardCore.Contents
      - OrchardCore.Commerce
  - id: OrchardCore.Commerce.CurrencySettingsSelector
    name: "Orchard Core Commerce - Currency Settings Selector"
    description: "Currency selector that uses display currency configured in settings. Useful for Dev/Test scenarios. Its upstream feature ID is `OrchardCore.Commerce.CurrencySettingsSelector`, and it is categorized as Commerce. It depends on `OrchardCore.Contents`, and `OrchardCore.Commerce`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core Commerce manifest metadata; Orchard Core displays feature entries in the feature management UI with their description, category, and dependencies."
    category: Commerce
    dependencies:
      - OrchardCore.Contents
      - OrchardCore.Commerce
  - id: OrchardCore.Commerce.Subscription
    name: "Orchard Core Commerce - Subscription"
    description: "Subscription management. Currently only supports Stripe. Its upstream feature ID is `OrchardCore.Commerce.Subscription`, and it is categorized as Commerce. It depends on `OrchardCore.Contents`, and `OrchardCore.Commerce`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core Commerce manifest metadata; Orchard Core displays feature entries in the feature management UI with their description, category, and dependencies."
    category: Commerce
    dependencies:
      - OrchardCore.Contents
      - OrchardCore.Commerce
  - id: OrchardCore.Commerce.SkuGenerator.Guid
    name: "Orchard Core Commerce - SKU Generator - GUID"
    description: "Replaces manual SKU entry in the content item editor with a GUID-based generator. Its upstream feature ID is `OrchardCore.Commerce.SkuGenerator.Guid`, and it is categorized as Commerce. It depends on `OrchardCore.Commerce`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core Commerce manifest metadata; Orchard Core displays feature entries in the feature management UI with their description, category, and dependencies."
    category: Commerce
    dependencies:
      - OrchardCore.Commerce
---
The commerce module for Orchard Core.

## Features

### Orchard Core Commerce - Core

Registers the core components used by the Commerce features. Its upstream feature ID is `OrchardCore.Commerce`, and it is categorized as Commerce. It depends on `OrchardCore.Contents`, `OrchardCore.Workflows`, `OrchardCore.Templates`, `OrchardCore.Commerce.ContentFields`, and `OrchardCore.Commerce.Payment`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core Commerce manifest metadata; Orchard Core displays feature entries in the feature management UI with their description, category, and dependencies.

### Orchard Core Commerce - Session Cart Storage

Registers session-based shopping cart persistence. Its upstream feature ID is `OrchardCore.Commerce.SessionCartStorage`, and it is categorized as Commerce. It depends on `OrchardCore.Contents`, and `OrchardCore.Commerce`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core Commerce manifest metadata; Orchard Core displays feature entries in the feature management UI with their description, category, and dependencies.

### Orchard Core Commerce - Currency Settings Selector

Currency selector that uses display currency configured in settings. Useful for Dev/Test scenarios. Its upstream feature ID is `OrchardCore.Commerce.CurrencySettingsSelector`, and it is categorized as Commerce. It depends on `OrchardCore.Contents`, and `OrchardCore.Commerce`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core Commerce manifest metadata; Orchard Core displays feature entries in the feature management UI with their description, category, and dependencies.

### Orchard Core Commerce - Subscription

Subscription management. Currently only supports Stripe. Its upstream feature ID is `OrchardCore.Commerce.Subscription`, and it is categorized as Commerce. It depends on `OrchardCore.Contents`, and `OrchardCore.Commerce`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core Commerce manifest metadata; Orchard Core displays feature entries in the feature management UI with their description, category, and dependencies.

### Orchard Core Commerce - SKU Generator - GUID

Replaces manual SKU entry in the content item editor with a GUID-based generator. Its upstream feature ID is `OrchardCore.Commerce.SkuGenerator.Guid`, and it is categorized as Commerce. It depends on `OrchardCore.Commerce`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core Commerce manifest metadata; Orchard Core displays feature entries in the feature management UI with their description, category, and dependencies.

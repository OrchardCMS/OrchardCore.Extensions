---
title: "Orchard Core Commerce - Payment - Stripe"
slug: OrchardCore.Commerce.Payment.Stripe
description:
  Stripe payment provider for Orchard Core Commerce. It helps Orchard Core sites add commerce capabilities while
  exposing package, dependency, source, and documentation details in the extensions gallery.
projectUrl: https://github.com/OrchardCMS/OrchardCore.Commerce/tree/main/src/Modules/OrchardCore.Commerce.Payment.Stripe
documentationUrl: https://docs.orchardcore.net
nuGetPackageId: OrchardCore.Commerce.Payment.Stripe
tags: ["Orchard Core", "Commerce", "e-Commerce", "Payment", "Stripe"]
author:
  name: The Orchard Core Team
  url: https://docs.orchardcore.net
  imageUrl: https://docs.orchardcore.net/en/latest/assets/images/favicon.png
licenses: [BSD-3-Clause]
pubDatetime: 2026-07-30T23:08:43Z
features:
  - id: OrchardCore.Commerce.Payment.Stripe
    name: "Orchard Core Commerce - Payment - Stripe"
    description: "Stripe payment provider for Orchard Core Commerce. Note: you must configure it in Admin > Configuration > Commerce > Stripe API or it won't appear in the front end. Its upstream feature ID is `OrchardCore.Commerce.Payment.Stripe`, and it is categorized as Commerce. It depends on `OrchardCore.Commerce.Payment`, `OrchardCore.Commerce.Promotion`, and `OrchardCore.Commerce.Subscription`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core Commerce manifest metadata; Orchard Core displays feature entries in the feature management UI with their description, category, and dependencies."
    category: Commerce
    dependencies:
      - OrchardCore.Commerce.Payment
      - OrchardCore.Commerce.Promotion
      - OrchardCore.Commerce.Subscription
  - id: OrchardCore.Commerce.Payment.Stripe.DummyStripeServices
    name: "Orchard Core Commerce - Payment - Stripe - Dummy Stripe Services"
    description: "WARNING: Only enable this feature in the UI testing environment. Simulates Stripe services for testing purposes. Its upstream feature ID is `OrchardCore.Commerce.Payment.Stripe.DummyStripeServices`, and it is categorized as Commerce. It depends on `OrchardCore.Commerce.Payment.Stripe`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core Commerce manifest metadata; Orchard Core displays feature entries in the feature management UI with their description, category, and dependencies."
    category: Commerce
    dependencies:
      - OrchardCore.Commerce.Payment.Stripe
---
Stripe payment provider for Orchard Core Commerce.

## Features

### Orchard Core Commerce - Payment - Stripe

Stripe payment provider for Orchard Core Commerce. Note: you must configure it in Admin > Configuration > Commerce > Stripe API or it won't appear in the front end. Its upstream feature ID is `OrchardCore.Commerce.Payment.Stripe`, and it is categorized as Commerce. It depends on `OrchardCore.Commerce.Payment`, `OrchardCore.Commerce.Promotion`, and `OrchardCore.Commerce.Subscription`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core Commerce manifest metadata; Orchard Core displays feature entries in the feature management UI with their description, category, and dependencies.

### Orchard Core Commerce - Payment - Stripe - Dummy Stripe Services

WARNING: Only enable this feature in the UI testing environment. Simulates Stripe services for testing purposes. Its upstream feature ID is `OrchardCore.Commerce.Payment.Stripe.DummyStripeServices`, and it is categorized as Commerce. It depends on `OrchardCore.Commerce.Payment.Stripe`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core Commerce manifest metadata; Orchard Core displays feature entries in the feature management UI with their description, category, and dependencies.

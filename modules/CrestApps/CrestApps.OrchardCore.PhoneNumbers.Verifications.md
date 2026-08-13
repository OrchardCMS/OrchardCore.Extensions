---
title: "Phone Number Verifications"
slug: CrestApps.OrchardCore.PhoneNumbers.Verifications
description:
  Provides the Phone Number Verifications module for Orchard Core. It includes Phone Number Verifications,
  AbstractAPI Phone Number Verification and related features in the Phone Verification area, making the package
  easier to find when browsing related Orchard Core capabilities, dependencies, and documentation.
projectUrl: https://github.com/CrestApps/CrestApps.OrchardCore/tree/main/src/Modules/CrestApps.OrchardCore.PhoneNumbers.Verifications
documentationUrl: https://orchardcore.crestapps.com
nuGetPackageId: CrestApps.OrchardCore.PhoneNumbers.Verifications
tags: ["crestapps", "Phone Verification"]
author:
  name: CrestApps
  url: https://crestapps.com
  imageUrl: https://avatars.githubusercontent.com/u/111536479
licenses: [MIT]
versions:
  - 2.x
  - 3.x
pubDatetime: 2026-08-12T12:00:00Z
features:
  - id: CrestApps.OrchardCore.PhoneNumbers.Verifications
    name: "Phone Number Verifications"
    description: "Provides a provider-agnostic framework for verifying phone numbers, storing results on contact content items, and background revalidation. Its manifest-backed feature ID is `CrestApps.OrchardCore.PhoneNumbers.Verifications`, and it is categorized as Phone Verification. It depends on `OrchardCore.Contents`, and `CrestApps.OrchardCore.PhoneNumbers`, so Orchard Core enables those dependencies when this feature is enabled. The manifest marks it as enabled by dependency only, so it is intended to support other features rather than be selected as a standalone end-user feature. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: "Phone Verification"
    dependencies:
      - OrchardCore.Contents
      - CrestApps.OrchardCore.PhoneNumbers
    enabledByDependencyOnly: true
  - id: CrestApps.OrchardCore.PhoneNumbers.Verifications.AbstractApi
    name: "AbstractAPI Phone Number Verification"
    description: "Verifies phone numbers using the AbstractAPI Phone Validation service. Its manifest-backed feature ID is `CrestApps.OrchardCore.PhoneNumbers.Verifications.AbstractApi`, and it is categorized as Phone Verification. It depends on `CrestApps.OrchardCore.PhoneNumbers.Verifications`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: "Phone Verification"
    dependencies:
      - CrestApps.OrchardCore.PhoneNumbers.Verifications
    documentationUrl: https://orchardcore.crestapps.com/docs/modules/phone-number-verifications-abstractapi
  - id: CrestApps.OrchardCore.PhoneNumbers.Verifications.Veriphone
    name: "Veriphone Phone Number Verification"
    description: "Verifies phone numbers using the Veriphone phone number validation service. Its manifest-backed feature ID is `CrestApps.OrchardCore.PhoneNumbers.Verifications.Veriphone`, and it is categorized as Phone Verification. It depends on `CrestApps.OrchardCore.PhoneNumbers.Verifications`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: "Phone Verification"
    dependencies:
      - CrestApps.OrchardCore.PhoneNumbers.Verifications
  - id: CrestApps.OrchardCore.PhoneNumbers.Verifications.Twilio
    name: "Twilio Phone Number Verification"
    description: "Verifies phone numbers using the Twilio Lookup service. Its manifest-backed feature ID is `CrestApps.OrchardCore.PhoneNumbers.Verifications.Twilio`, and it is categorized as Phone Verification. It depends on `CrestApps.OrchardCore.PhoneNumbers.Verifications`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: "Phone Verification"
    dependencies:
      - CrestApps.OrchardCore.PhoneNumbers.Verifications
    documentationUrl: https://orchardcore.crestapps.com/docs/modules/phone-number-verifications-twilio
---
Provides the Phone Number Verifications module for Orchard Core.

## Features

### Phone Number Verifications

Provides a provider-agnostic framework for verifying phone numbers, storing results on contact content items, and background revalidation. Its manifest-backed feature ID is `CrestApps.OrchardCore.PhoneNumbers.Verifications`, and it is categorized as Phone Verification. It depends on `OrchardCore.Contents`, and `CrestApps.OrchardCore.PhoneNumbers`, so Orchard Core enables those dependencies when this feature is enabled. The manifest marks it as enabled by dependency only, so it is intended to support other features rather than be selected as a standalone end-user feature. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### AbstractAPI Phone Number Verification

Verifies phone numbers using the AbstractAPI Phone Validation service. Its manifest-backed feature ID is `CrestApps.OrchardCore.PhoneNumbers.Verifications.AbstractApi`, and it is categorized as Phone Verification. It depends on `CrestApps.OrchardCore.PhoneNumbers.Verifications`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Veriphone Phone Number Verification

Verifies phone numbers using the Veriphone phone number validation service. Its manifest-backed feature ID is `CrestApps.OrchardCore.PhoneNumbers.Verifications.Veriphone`, and it is categorized as Phone Verification. It depends on `CrestApps.OrchardCore.PhoneNumbers.Verifications`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Twilio Phone Number Verification

Verifies phone numbers using the Twilio Lookup service. Its manifest-backed feature ID is `CrestApps.OrchardCore.PhoneNumbers.Verifications.Twilio`, and it is categorized as Phone Verification. It depends on `CrestApps.OrchardCore.PhoneNumbers.Verifications`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

---
title: "DNC Registry"
slug: CrestApps.OrchardCore.DncRegistry
description: "Provides the DNC Registry module for Orchard Core."
projectUrl: https://github.com/CrestApps/CrestApps.OrchardCore/tree/main/src/Modules/CrestApps.OrchardCore.DncRegistry
documentationUrl: https://orchardcore.crestapps.com/docs/modules/dnc-registry
nuGetPackageId: CrestApps.OrchardCore.DncRegistry
tags: ["CrestApps", "Compliance"]
author:
  name: The CrestApps Team
  url: https://www.crestapps.com
  imageUrl: https://avatars.githubusercontent.com/u/181091452
licenses: [MIT]
pubDatetime: 2026-08-12T12:00:00Z
features:
  - id: CrestApps.OrchardCore.DncRegistry
    name: "DNC Registry"
    description: "Provides the core framework for integrating with national do-not-call registries. Its manifest-backed feature ID is `CrestApps.OrchardCore.DncRegistry`, and it is categorized as Compliance. It depends on `CrestApps.OrchardCore.PhoneNumbers`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: "Compliance"
    dependencies:
      - CrestApps.OrchardCore.PhoneNumbers
  - id: CrestApps.OrchardCore.DncRegistry.UsaFtc
    name: "USA FTC Do Not Call Registry"
    description: "Integrates with the United States Federal Trade Commission (FTC) National Do Not Call Registry at telemarketing.donotcall.gov. Its manifest-backed feature ID is `CrestApps.OrchardCore.DncRegistry.UsaFtc`, and it is categorized as Compliance. It depends on `CrestApps.OrchardCore.DncRegistry`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: "Compliance"
    dependencies:
      - CrestApps.OrchardCore.DncRegistry
  - id: CrestApps.OrchardCore.DncRegistry.CanadaDncl
    name: "Canada LNNTE-DNCL Registry"
    description: "Integrates with the Canadian National Do Not Call List (LNNTE-DNCL) maintained by the CRTC. Its manifest-backed feature ID is `CrestApps.OrchardCore.DncRegistry.CanadaDncl`, and it is categorized as Compliance. It depends on `CrestApps.OrchardCore.DncRegistry`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: "Compliance"
    dependencies:
      - CrestApps.OrchardCore.DncRegistry
  - id: CrestApps.OrchardCore.DncRegistry.Local
    name: "Local Do Not Call Registry"
    description: "Provides a local do-not-call registry where administrators can upload CSV files of phone numbers organized by country. Its manifest-backed feature ID is `CrestApps.OrchardCore.DncRegistry.Local`, and it is categorized as Compliance. It depends on `CrestApps.OrchardCore.DncRegistry`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: "Compliance"
    dependencies:
      - CrestApps.OrchardCore.DncRegistry
---
Provides the DNC Registry module for Orchard Core.

## Features

### DNC Registry

Provides the core framework for integrating with national do-not-call registries. Its manifest-backed feature ID is `CrestApps.OrchardCore.DncRegistry`, and it is categorized as Compliance. It depends on `CrestApps.OrchardCore.PhoneNumbers`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### USA FTC Do Not Call Registry

Integrates with the United States Federal Trade Commission (FTC) National Do Not Call Registry at telemarketing.donotcall.gov. Its manifest-backed feature ID is `CrestApps.OrchardCore.DncRegistry.UsaFtc`, and it is categorized as Compliance. It depends on `CrestApps.OrchardCore.DncRegistry`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Canada LNNTE-DNCL Registry

Integrates with the Canadian National Do Not Call List (LNNTE-DNCL) maintained by the CRTC. Its manifest-backed feature ID is `CrestApps.OrchardCore.DncRegistry.CanadaDncl`, and it is categorized as Compliance. It depends on `CrestApps.OrchardCore.DncRegistry`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Local Do Not Call Registry

Provides a local do-not-call registry where administrators can upload CSV files of phone numbers organized by country. Its manifest-backed feature ID is `CrestApps.OrchardCore.DncRegistry.Local`, and it is categorized as Compliance. It depends on `CrestApps.OrchardCore.DncRegistry`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the CrestApps manifest and documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

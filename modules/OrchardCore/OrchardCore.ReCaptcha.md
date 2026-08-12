---
title: ReCaptcha
slug: OrchardCore.ReCaptcha
description:
  Provides core ReCaptcha functionality. It includes ReCaptcha and ReCaptcha Users features in the Security
  area, making the package easier to find when browsing related Orchard Core capabilities, dependencies, and
  documentation.
projectUrl: https://github.com/OrchardCMS/OrchardCore/tree/main/src/OrchardCore.Modules/OrchardCore.ReCaptcha
documentationUrl: https://docs.orchardcore.net
nuGetPackageId: OrchardCore.ReCaptcha
tags: ["Orchard Core"]
author:
  name: The Orchard Core Team
  url: https://docs.orchardcore.net
  imageUrl: https://docs.orchardcore.net/en/latest/assets/images/favicon.png
licenses: [BSD-3-Clause]
pubDatetime: 2026-08-12T12:00:00Z
features:
  - id: OrchardCore.ReCaptcha
    name: ReCaptcha
    description: "Provides core ReCaptcha functionality. Its manifest-backed feature ID is `OrchardCore.ReCaptcha`, and it is categorized as Security. No additional feature dependencies are listed for it in this catalog entry. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Security
  - id: OrchardCore.ReCaptcha.Users
    name: ReCaptcha Users
    description: "Provides ReCaptcha functionality to harness login, register, forgot password and forms against robots. Its manifest-backed feature ID is `OrchardCore.ReCaptcha.Users`, and it is categorized as Security. It depends on `OrchardCore.ReCaptcha`, and `OrchardCore.Users`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Security
    dependencies:
      - OrchardCore.ReCaptcha
      - OrchardCore.Users
---
Provides core ReCaptcha functionality.

## Features

### ReCaptcha

Provides core ReCaptcha functionality. Its manifest-backed feature ID is `OrchardCore.ReCaptcha`, and it is categorized as Security. No additional feature dependencies are listed for it in this catalog entry. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### ReCaptcha Users

Provides ReCaptcha functionality to harness login, register, forgot password and forms against robots. Its manifest-backed feature ID is `OrchardCore.ReCaptcha.Users`, and it is categorized as Security. It depends on `OrchardCore.ReCaptcha`, and `OrchardCore.Users`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

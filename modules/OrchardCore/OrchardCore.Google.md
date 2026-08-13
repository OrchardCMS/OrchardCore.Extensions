---
title: Google
slug: OrchardCore.Google
description:
  Authenticates users with their Google Account. It includes Google Authentication, Google Analytics and Google
  Tag Manager features in the Google area, making the package easier to find when browsing related Orchard Core
  capabilities, dependencies, and documentation.
projectUrl: https://github.com/OrchardCMS/OrchardCore/tree/main/src/OrchardCore.Modules/OrchardCore.Google
documentationUrl: https://docs.orchardcore.net
nuGetPackageId: OrchardCore.Google
tags: ["Orchard Core", "Google"]
author:
  name: The Orchard Core Team
  url: https://docs.orchardcore.net
  imageUrl: https://docs.orchardcore.net/en/latest/assets/images/favicon.png
licenses: [BSD-3-Clause]
compatibleWithAllVersions: true
pubDatetime: 2026-08-12T12:00:00Z
features:
  - id: OrchardCore.Google.GoogleAuthentication
    name: Google Authentication
    description: "Authenticates users with their Google Account. Its manifest-backed feature ID is `OrchardCore.Google.GoogleAuthentication`, and it is categorized as Google. It depends on `OrchardCore.Users.ExternalAuthentication`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Google
    dependencies:
      - OrchardCore.Users.ExternalAuthentication
  - id: OrchardCore.Google.Analytics
    name: Google Analytics
    description: "Integrate Google Analytics (gtag.js). Its manifest-backed feature ID is `OrchardCore.Google.Analytics`, and it is categorized as Google. No additional feature dependencies are listed for it in this catalog entry. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Google
  - id: OrchardCore.Google.TagManager
    name: Google Tag Manager
    description: "Integrate Google Tag Manager. Its manifest-backed feature ID is `OrchardCore.Google.TagManager`, and it is categorized as Google. No additional feature dependencies are listed for it in this catalog entry. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Google
---
Authenticates users with their Google Account.

## Features

### Google Authentication

Authenticates users with their Google Account. Its manifest-backed feature ID is `OrchardCore.Google.GoogleAuthentication`, and it is categorized as Google. It depends on `OrchardCore.Users.ExternalAuthentication`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Google Analytics

Integrate Google Analytics (gtag.js). Its manifest-backed feature ID is `OrchardCore.Google.Analytics`, and it is categorized as Google. No additional feature dependencies are listed for it in this catalog entry. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Google Tag Manager

Integrate Google Tag Manager. Its manifest-backed feature ID is `OrchardCore.Google.TagManager`, and it is categorized as Google. No additional feature dependencies are listed for it in this catalog entry. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

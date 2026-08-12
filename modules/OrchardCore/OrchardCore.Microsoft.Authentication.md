---
title: Microsoft Authentication
slug: OrchardCore.Microsoft.Authentication
description:
  Authenticates users with their Microsoft Account. It includes Microsoft Account Authentication and Microsoft
  Entra ID (Azure Active Directory) Authentication features in the Microsoft Authentication area, making the
  package easier to find when browsing related Orchard Core capabilities, dependencies, and documentation.
projectUrl: https://github.com/OrchardCMS/OrchardCore/tree/main/src/OrchardCore.Modules/OrchardCore.Microsoft.Authentication
documentationUrl: https://docs.orchardcore.net/en/latest/reference/modules/Microsoft.Authentication/
nuGetPackageId: OrchardCore.Microsoft.Authentication
tags: ["Orchard Core", "Microsoft Authentication"]
author:
  name: The Orchard Core Team
  url: https://docs.orchardcore.net
  imageUrl: https://docs.orchardcore.net/en/latest/assets/images/orchard-logo.png
licenses: [BSD-3-Clause]
pubDatetime: 2026-08-12T12:00:00Z
features:
  - id: OrchardCore.Microsoft.Authentication.MicrosoftAccount
    name: Microsoft Account Authentication
    description: "Authenticates users with their Microsoft Account. Its manifest-backed feature ID is `OrchardCore.Microsoft.Authentication.MicrosoftAccount`, and it is categorized as Microsoft Authentication. It depends on `OrchardCore.Users.ExternalAuthentication`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Microsoft Authentication
    dependencies:
      - OrchardCore.Users.ExternalAuthentication
  - id: OrchardCore.Microsoft.Authentication.AzureAD
    name: Microsoft Entra ID (Azure Active Directory) Authentication
    description: "Authenticates users with their Microsoft Entra ID Account. Its manifest-backed feature ID is `OrchardCore.Microsoft.Authentication.AzureAD`, and it is categorized as Microsoft Authentication. It depends on `OrchardCore.Users.ExternalAuthentication`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Microsoft Authentication
    dependencies:
      - OrchardCore.Users.ExternalAuthentication
---
Authenticates users with their Microsoft Account.

## Features

### Microsoft Account Authentication

Authenticates users with their Microsoft Account. Its manifest-backed feature ID is `OrchardCore.Microsoft.Authentication.MicrosoftAccount`, and it is categorized as Microsoft Authentication. It depends on `OrchardCore.Users.ExternalAuthentication`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Microsoft Entra ID (Azure Active Directory) Authentication

Authenticates users with their Microsoft Entra ID Account. Its manifest-backed feature ID is `OrchardCore.Microsoft.Authentication.AzureAD`, and it is categorized as Microsoft Authentication. It depends on `OrchardCore.Users.ExternalAuthentication`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

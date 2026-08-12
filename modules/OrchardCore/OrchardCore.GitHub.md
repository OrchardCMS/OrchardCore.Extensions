---
title: GitHub
slug: OrchardCore.GitHub
description:
  Authenticates users with their GitHub Account. It helps site owners add this capability to Orchard Core sites
  while exposing package, dependency, and documentation details in the extensions gallery.
projectUrl: https://github.com/OrchardCMS/OrchardCore/tree/main/src/OrchardCore.Modules/OrchardCore.GitHub
documentationUrl: https://docs.orchardcore.net/en/latest/reference/modules/GitHub/
nuGetPackageId: OrchardCore.GitHub
tags: ["Orchard Core", "GitHub"]
author:
  name: The Orchard Core Team
  url: https://docs.orchardcore.net
  imageUrl: https://docs.orchardcore.net/en/latest/assets/images/orchard-logo.png
licenses: [BSD-3-Clause]
pubDatetime: 2026-08-12T12:00:00Z
features:
  - id: OrchardCore.GitHub.Authentication
    name: GitHub Authentication
    description: "Authenticates users with their GitHub Account. Its manifest-backed feature ID is `OrchardCore.GitHub.Authentication`, and it is categorized as GitHub. It depends on `OrchardCore.Users.ExternalAuthentication`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: GitHub
    dependencies:
      - OrchardCore.Users.ExternalAuthentication
---
Authenticates users with their GitHub Account.

## Features

### GitHub Authentication

Authenticates users with their GitHub Account. Its manifest-backed feature ID is `OrchardCore.GitHub.Authentication`, and it is categorized as GitHub. It depends on `OrchardCore.Users.ExternalAuthentication`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

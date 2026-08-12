---
title: Twitter
slug: OrchardCore.Twitter
description:
  Provides a TwitterClient and Workflow Activities to integrate with X (Twitter)
projectUrl: https://github.com/OrchardCMS/OrchardCore/tree/main/src/OrchardCore.Modules/OrchardCore.Twitter
documentationUrl: https://docs.orchardcore.net/en/latest/reference/modules/Twitter/
nuGetPackageId: OrchardCore.Twitter
tags: ["Orchard Core", "X (Twitter)"]
author:
  name: The Orchard Core Team
  url: https://github.com/OrchardCMS
  imageUrl: https://avatars.githubusercontent.com/u/9933239
licenses: [BSD-3-Clause]
pubDatetime: 2026-08-12T12:00:00Z
features:
  - id: OrchardCore.Twitter
    name: X (Twitter) Integration
    description: "Provides a TwitterClient and Workflow Activities to integrate with X (Twitter). Its manifest-backed feature ID is `OrchardCore.Twitter`, and it is categorized as X (Twitter). No additional feature dependencies are listed for it in this catalog entry. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: X (Twitter)
  - id: OrchardCore.Twitter.Signin
    name: Sign in with X (Twitter)
    description: "Authenticates users with their X (Twitter) Account. Its manifest-backed feature ID is `OrchardCore.Twitter.Signin`, and it is categorized as X (Twitter). It depends on `OrchardCore.Twitter`, and `OrchardCore.Users.ExternalAuthentication`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: X (Twitter)
    dependencies:
      - OrchardCore.Twitter
      - OrchardCore.Users.ExternalAuthentication
---
Provides a TwitterClient and Workflow Activities to integrate with X (Twitter)

## Features

### X (Twitter) Integration

Provides a TwitterClient and Workflow Activities to integrate with X (Twitter). Its manifest-backed feature ID is `OrchardCore.Twitter`, and it is categorized as X (Twitter). No additional feature dependencies are listed for it in this catalog entry. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Sign in with X (Twitter)

Authenticates users with their X (Twitter) Account. Its manifest-backed feature ID is `OrchardCore.Twitter.Signin`, and it is categorized as X (Twitter). It depends on `OrchardCore.Twitter`, and `OrchardCore.Users.ExternalAuthentication`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

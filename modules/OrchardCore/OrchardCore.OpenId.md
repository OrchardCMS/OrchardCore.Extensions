---
title: OpenID Connect
slug: OrchardCore.OpenId
description:
  Provides the foundational services for all OpenID Connect features. It includes OpenID Connect Core Services,
  OpenID Connect Client Integration and related features in the OpenID Connect area, making the package easier
  to find when browsing related Orchard Core capabilities, dependencies, and documentation.
projectUrl: https://github.com/OrchardCMS/OrchardCore/tree/main/src/OrchardCore.Modules/OrchardCore.OpenId
documentationUrl: https://docs.orchardcore.net/en/latest/reference/modules/OpenId/
nuGetPackageId: OrchardCore.OpenId
tags: ["Orchard Core"]
author:
  name: The Orchard Core Team
  url: https://docs.orchardcore.net
  imageUrl: https://docs.orchardcore.net/en/latest/assets/images/orchard-logo.png
licenses: [BSD-3-Clause]
pubDatetime: 2026-08-12T12:00:00Z
features:
  - id: OrchardCore.OpenId
    name: OpenID Connect Core Services
    description: "Provides the foundational services for all OpenID Connect features. Its manifest-backed feature ID is `OrchardCore.OpenId`, and it is categorized as OpenID Connect. No additional feature dependencies are listed for it in this catalog entry. The manifest marks it as enabled by dependency only, so it is intended to support other features rather than be selected as a standalone end-user feature. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: OpenID Connect
    enabledByDependencyOnly: true
  - id: OrchardCore.OpenId.Client
    name: OpenID Connect Client Integration
    description: "Allows authentication of users through an external OpenID Connect authorization server (also known as an identity provider). Its manifest-backed feature ID is `OrchardCore.OpenId.Client`, and it is categorized as OpenID Connect. It depends on `OrchardCore.OpenId`, and `OrchardCore.Users.ExternalAuthentication`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: OpenID Connect
    dependencies:
      - OrchardCore.OpenId
      - OrchardCore.Users.ExternalAuthentication
  - id: OrchardCore.OpenId.Management
    name: OpenID Connect Management UI
    description: "Adds a user interface for managing OpenID Connect applications, scopes and permissions. Its manifest-backed feature ID is `OrchardCore.OpenId.Management`, and it is categorized as OpenID Connect. It depends on `OrchardCore.OpenId`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: OpenID Connect
    dependencies:
      - OrchardCore.OpenId
  - id: OrchardCore.OpenId.Server
    name: OpenID Connect Authorization Server
    description: "Enables Orchard Core to function as an OpenID Connect authorization server/identity provider, supporting authentication and token issuance using OpenID Connect and OAuth 2.0 standards. To enable token validation, activate the 'OpenID Connect Token Validation' feature. Its manifest-backed feature ID is `OrchardCore.OpenId.Server`, and it is categorized as OpenID Connect. It depends on `OrchardCore.OpenId`, and `OrchardCore.OpenId.Management`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: OpenID Connect
    dependencies:
      - OrchardCore.OpenId
      - OrchardCore.OpenId.Management
  - id: OrchardCore.OpenId.Validation
    name: OpenID Connect Token Validation
    description: "Validates tokens issued by the local OpenID Connect authorization server or other trusted servers supporting JWT and OpenID Connect discovery. Its manifest-backed feature ID is `OrchardCore.OpenId.Validation`, and it is categorized as OpenID Connect. It depends on `OrchardCore.OpenId`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: OpenID Connect
    dependencies:
      - OrchardCore.OpenId
---
Provides the foundational services for all OpenID Connect features.

## Features

### OpenID Connect Core Services

Provides the foundational services for all OpenID Connect features. Its manifest-backed feature ID is `OrchardCore.OpenId`, and it is categorized as OpenID Connect. No additional feature dependencies are listed for it in this catalog entry. The manifest marks it as enabled by dependency only, so it is intended to support other features rather than be selected as a standalone end-user feature. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### OpenID Connect Client Integration

Allows authentication of users through an external OpenID Connect authorization server (also known as an identity provider). Its manifest-backed feature ID is `OrchardCore.OpenId.Client`, and it is categorized as OpenID Connect. It depends on `OrchardCore.OpenId`, and `OrchardCore.Users.ExternalAuthentication`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### OpenID Connect Management UI

Adds a user interface for managing OpenID Connect applications, scopes and permissions. Its manifest-backed feature ID is `OrchardCore.OpenId.Management`, and it is categorized as OpenID Connect. It depends on `OrchardCore.OpenId`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### OpenID Connect Authorization Server

Enables Orchard Core to function as an OpenID Connect authorization server/identity provider, supporting authentication and token issuance using OpenID Connect and OAuth 2.0 standards. To enable token validation, activate the 'OpenID Connect Token Validation' feature. Its manifest-backed feature ID is `OrchardCore.OpenId.Server`, and it is categorized as OpenID Connect. It depends on `OrchardCore.OpenId`, and `OrchardCore.OpenId.Management`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### OpenID Connect Token Validation

Validates tokens issued by the local OpenID Connect authorization server or other trusted servers supporting JWT and OpenID Connect discovery. Its manifest-backed feature ID is `OrchardCore.OpenId.Validation`, and it is categorized as OpenID Connect. It depends on `OrchardCore.OpenId`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

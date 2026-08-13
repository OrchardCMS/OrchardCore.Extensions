---
title: "Users (Contrib)"
slug: OrchardCoreContrib.Users
description:
  Provides a list of users features such as Impersonation. It helps Orchard Core sites add this
  community-maintained capability while exposing package, dependency, source, and documentation details in the
  extensions gallery.
projectUrl: https://github.com/OrchardCoreContrib/OrchardCoreContrib.Modules/blob/main/src/OrchardCoreContrib.Users/README.md
documentationUrl: https://github.com/OrchardCoreContrib/OrchardCoreContrib.Modules/blob/main/src/OrchardCoreContrib.Users/README.md
nuGetPackageId: OrchardCoreContrib.Users
tags: ["Orchard Core", "Users"]
author:
  name: OrchardCoreContrib
  url: https://github.com/OrchardCoreContrib
  imageUrl: https://avatars.githubusercontent.com/u/65380704
licenses: [BSD-3-Clause]
versions:
  - orchard: 1.x
  - orchard: 2.x
pubDatetime: 2026-08-12T18:01:00Z
features:
  - id: OrchardCoreContrib.Users.Avatar
    name: "User Avatar"
    description: "This feature allow to display a user avatar on the admin menu. Its upstream feature ID is `OrchardCoreContrib.Users.Avatar`, and it is categorized as Users. It depends on `OrchardCore.Users`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the OrchardCoreContrib manifest metadata; Orchard Core displays feature entries in the feature management UI with their description, category, and dependencies."
    category: "Users"
    dependencies:
      - OrchardCore.Users
  - id: OrchardCoreContrib.Users.Impersonation
    name: "Users Impersonation"
    description: "This feature allow administrators to sign in with other user identity. Its upstream feature ID is `OrchardCoreContrib.Users.Impersonation`, and it is categorized as Users. It depends on `OrchardCore.Users`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the OrchardCoreContrib manifest metadata; Orchard Core displays feature entries in the feature management UI with their description, category, and dependencies."
    category: "Users"
    dependencies:
      - OrchardCore.Users
---
Provides a list of users features such as Impersonation.

## Features

### User Avatar

This feature allow to display a user avatar on the admin menu. Its upstream feature ID is `OrchardCoreContrib.Users.Avatar`, and it is categorized as Users. It depends on `OrchardCore.Users`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the OrchardCoreContrib manifest metadata; Orchard Core displays feature entries in the feature management UI with their description, category, and dependencies.

### Users Impersonation

This feature allow administrators to sign in with other user identity. Its upstream feature ID is `OrchardCoreContrib.Users.Impersonation`, and it is categorized as Users. It depends on `OrchardCore.Users`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the OrchardCoreContrib manifest metadata; Orchard Core displays feature entries in the feature management UI with their description, category, and dependencies.

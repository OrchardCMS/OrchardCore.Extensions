---
title: Content Fields
slug: OrchardCore.ContentFields
description:
  Content Fields module adds common content fields to be used with your custom types.
projectUrl: https://github.com/OrchardCMS/OrchardCore/tree/main/src/OrchardCore.Modules/OrchardCore.ContentFields
documentationUrl: https://docs.orchardcore.net/en/latest/reference/modules/ContentFields/
nuGetPackageId: OrchardCore.ContentFields
tags: ["Orchard Core", "Content Management"]
author:
  name: The Orchard Core Team
  url: https://github.com/OrchardCMS
  imageUrl: https://avatars.githubusercontent.com/u/9933239
licenses: [BSD-3-Clause]
pubDatetime: 2026-08-12T12:00:00Z
features:
  - id: OrchardCore.ContentFields
    name: Content Fields
    description: "Content Fields module adds common content fields to be used with your custom types. Its manifest-backed feature ID is `OrchardCore.ContentFields`, and it is categorized as Content Management. It depends on `OrchardCore.ContentTypes`, and `OrchardCore.Shortcodes`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Content Management
    dependencies:
      - OrchardCore.ContentTypes
      - OrchardCore.Shortcodes
  - id: OrchardCore.ContentFields.Indexing.SQL
    name: Content Fields Indexing (SQL)
    description: "Content Fields Indexing module adds database indexing for content fields. Its manifest-backed feature ID is `OrchardCore.ContentFields.Indexing.SQL`, and it is categorized as Content Management. It depends on `OrchardCore.ContentFields`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Content Management
    dependencies:
      - OrchardCore.ContentFields
  - id: OrchardCore.ContentFields.Indexing.SQL.UserPicker
    name: Content Fields Indexing (SQL) - User Picker
    description: "User Picker Content Fields Indexing module adds database indexing for user picker fields. Its manifest-backed feature ID is `OrchardCore.ContentFields.Indexing.SQL.UserPicker`, and it is categorized as Content Management. It depends on `OrchardCore.ContentFields`, and `OrchardCore.Users`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Content Management
    dependencies:
      - OrchardCore.ContentFields
      - OrchardCore.Users
---
Content Fields module adds common content fields to be used with your custom types.

## Features

### Content Fields

Content Fields module adds common content fields to be used with your custom types. Its manifest-backed feature ID is `OrchardCore.ContentFields`, and it is categorized as Content Management. It depends on `OrchardCore.ContentTypes`, and `OrchardCore.Shortcodes`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Content Fields Indexing (SQL)

Content Fields Indexing module adds database indexing for content fields. Its manifest-backed feature ID is `OrchardCore.ContentFields.Indexing.SQL`, and it is categorized as Content Management. It depends on `OrchardCore.ContentFields`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Content Fields Indexing (SQL) - User Picker

User Picker Content Fields Indexing module adds database indexing for user picker fields. Its manifest-backed feature ID is `OrchardCore.ContentFields.Indexing.SQL.UserPicker`, and it is categorized as Content Management. It depends on `OrchardCore.ContentFields`, and `OrchardCore.Users`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

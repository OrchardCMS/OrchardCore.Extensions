---
title: Shortcodes
slug: OrchardCore.Shortcodes
description:
  The Shortcodes feature adds shortcode capabilities. It includes Shortcodes and Shortcode Templates features in
  the Infrastructure and Content area, making the package easier to find when browsing related Orchard Core
  capabilities, dependencies, and documentation.
projectUrl: https://github.com/OrchardCMS/OrchardCore/tree/main/src/OrchardCore.Modules/OrchardCore.Shortcodes
documentationUrl: https://docs.orchardcore.net/en/latest/reference/modules/Shortcodes/
nuGetPackageId: OrchardCore.Shortcodes
tags: ["Orchard Core"]
author:
  name: The Orchard Core Team
  url: https://docs.orchardcore.net
  imageUrl: https://docs.orchardcore.net/en/latest/assets/images/orchard-logo.png
licenses: [BSD-3-Clause]
pubDatetime: 2026-08-12T12:00:00Z
features:
  - id: OrchardCore.Shortcodes
    name: Shortcodes
    description: "The Shortcodes feature adds shortcode capabilities. Its manifest-backed feature ID is `OrchardCore.Shortcodes`, and it is categorized as Infrastructure. No additional feature dependencies are listed for it in this catalog entry. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Infrastructure
  - id: OrchardCore.Shortcodes.Templates
    name: Shortcode Templates
    description: "The Shortcode Templates feature provides a way to write custom shortcode templates from the admin. Its manifest-backed feature ID is `OrchardCore.Shortcodes.Templates`, and it is categorized as Content. It depends on `OrchardCore.Liquid`, and `OrchardCore.Shortcodes`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Content
    dependencies:
      - OrchardCore.Liquid
      - OrchardCore.Shortcodes
---
The Shortcodes feature adds shortcode capabilities.

## Features

### Shortcodes

The Shortcodes feature adds shortcode capabilities. Its manifest-backed feature ID is `OrchardCore.Shortcodes`, and it is categorized as Infrastructure. No additional feature dependencies are listed for it in this catalog entry. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Shortcode Templates

The Shortcode Templates feature provides a way to write custom shortcode templates from the admin. Its manifest-backed feature ID is `OrchardCore.Shortcodes.Templates`, and it is categorized as Content. It depends on `OrchardCore.Liquid`, and `OrchardCore.Shortcodes`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

---
title: "Orchard Core Contrib - Content Preview"
slug: OrchardCoreContrib.ContentPreview
description:
  Provides a list of content preview features such as page preview bar. It helps Orchard Core sites add this
  community-maintained capability while exposing package, dependency, source, and documentation details in the
  extensions gallery.
projectUrl: https://github.com/OrchardCoreContrib/OrchardCoreContrib.Modules/blob/main/src/OrchardCoreContrib.ContentPreview/README.md
documentationUrl: https://github.com/OrchardCoreContrib/OrchardCoreContrib.Modules/blob/main/src/OrchardCoreContrib.ContentPreview/README.md
nuGetPackageId: OrchardCoreContrib.ContentPreview
tags: ["Orchard Core", "Page Preview"]
author:
  name: OrchardCoreContrib
  url: https://github.com/OrchardCoreContrib
  imageUrl: https://avatars.githubusercontent.com/u/65380704
licenses: [BSD-3-Clause]
pubDatetime: 2026-07-17T18:28:09Z
features:
  - id: Constants.PagePreviewBarFeatureId
    name: "Page Preview Bar"
    description: "Shows a top bar that allows you to preview the current page in desktop, tablet and mobile. Its upstream feature ID is `Constants.PagePreviewBarFeatureId`, and it is categorized as Page Preview. It depends on `OrchardCore.Resources`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the OrchardCoreContrib manifest metadata; Orchard Core displays feature entries in the feature management UI with their description, category, and dependencies."
    category: "Page Preview"
    dependencies:
      - OrchardCore.Resources
---
Provides a list of content preview features such as page preview bar.

## Features

### Page Preview Bar

Shows a top bar that allows you to preview the current page in desktop, tablet and mobile. Its upstream feature ID is `Constants.PagePreviewBarFeatureId`, and it is categorized as Page Preview. It depends on `OrchardCore.Resources`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the OrchardCoreContrib manifest metadata; Orchard Core displays feature entries in the feature management UI with their description, category, and dependencies.

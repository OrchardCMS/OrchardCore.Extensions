---
title: "HTML (Contrib)"
slug: OrchardCoreContrib.Html
description:
  The Html module enables content items to have rich content using Grapes JS. It helps Orchard Core sites add
  this community-maintained capability while exposing package, dependency, source, and documentation details in
  the extensions gallery.
projectUrl: https://github.com/OrchardCoreContrib/OrchardCoreContrib.Modules/blob/main/src/OrchardCoreContrib.Html/README.md
documentationUrl: https://github.com/OrchardCoreContrib/OrchardCoreContrib.Modules/blob/main/src/OrchardCoreContrib.Html/README.md
nuGetPackageId: OrchardCoreContrib.Html
tags: ["Orchard Core", "HTML", "Grapes JS"]
author:
  name: OrchardCoreContrib
  url: https://github.com/OrchardCoreContrib
  imageUrl: https://avatars.githubusercontent.com/u/65380704
licenses: [BSD-3-Clause]
versions:
  - orchard: 1.x
  - orchard: 2.x
pubDatetime: 2026-07-17T18:28:09Z
features:
  - id: OrchardCoreContrib.Html.GrapesJS
    name: "GrapesJS HTML Editor"
    description: "Enables GrapesJS editor for HtmlBody content. Its upstream feature ID is `OrchardCoreContrib.Html.GrapesJS`, and it is categorized as Content Management. It depends on `OrchardCore.Html`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the OrchardCoreContrib manifest metadata; Orchard Core displays feature entries in the feature management UI with their description, category, and dependencies."
    category: "Content Management"
    dependencies:
      - OrchardCore.Html
---
The Html module enables content items to have rich content using Grapes JS.

## Features

### GrapesJS HTML Editor

Enables GrapesJS editor for HtmlBody content. Its upstream feature ID is `OrchardCoreContrib.Html.GrapesJS`, and it is categorized as Content Management. It depends on `OrchardCore.Html`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the OrchardCoreContrib manifest metadata; Orchard Core displays feature entries in the feature management UI with their description, category, and dependencies.

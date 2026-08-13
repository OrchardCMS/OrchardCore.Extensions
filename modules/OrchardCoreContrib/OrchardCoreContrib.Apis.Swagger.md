---
title: "Swagger"
slug: OrchardCoreContrib.Apis.Swagger
description:
  Enables swagger documentation for Orchard Core APIs. It helps Orchard Core sites add this community-maintained
  capability while exposing package, dependency, source, and documentation details in the extensions gallery.
projectUrl: https://github.com/OrchardCoreContrib/OrchardCoreContrib.Modules/blob/main/src/OrchardCoreContrib.Apis.Swagger/README.md
documentationUrl: https://github.com/OrchardCoreContrib/OrchardCoreContrib.Modules/blob/main/src/OrchardCoreContrib.Apis.Swagger/README.md
nuGetPackageId: OrchardCoreContrib.Apis.Swagger
tags: ["Orchard Core", "OpenAPI", "Swagger", "Swagger UI"]
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
  - id: OrchardCoreContrib.Apis.Swagger
    name: "Swagger"
    description: "Enables Swagger for Orchard Core APIs. Its upstream feature ID is `OrchardCoreContrib.Apis.Swagger`, and it is categorized as OpenAPI. No additional feature dependencies are listed for it in the upstream manifest. This description is based on the OrchardCoreContrib manifest metadata; Orchard Core displays feature entries in the feature management UI with their description, category, and dependencies."
    category: "OpenAPI"
  - id: OrchardCoreContrib.Apis.Swagger.UI
    name: "Swagger UI"
    description: "Enables Swagger UI for Orchard Core APIs. Its upstream feature ID is `OrchardCoreContrib.Apis.Swagger.UI`, and it is categorized as OpenAPI. It depends on `OrchardCoreContrib.Apis.Swagger`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the OrchardCoreContrib manifest metadata; Orchard Core displays feature entries in the feature management UI with their description, category, and dependencies."
    category: "OpenAPI"
    dependencies:
      - OrchardCoreContrib.Apis.Swagger
---
Enables swagger documentation for Orchard Core APIs.

## Features

### Swagger

Enables Swagger for Orchard Core APIs. Its upstream feature ID is `OrchardCoreContrib.Apis.Swagger`, and it is categorized as OpenAPI. No additional feature dependencies are listed for it in the upstream manifest. This description is based on the OrchardCoreContrib manifest metadata; Orchard Core displays feature entries in the feature management UI with their description, category, and dependencies.

### Swagger UI

Enables Swagger UI for Orchard Core APIs. Its upstream feature ID is `OrchardCoreContrib.Apis.Swagger.UI`, and it is categorized as OpenAPI. It depends on `OrchardCoreContrib.Apis.Swagger`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the OrchardCoreContrib manifest metadata; Orchard Core displays feature entries in the feature management UI with their description, category, and dependencies.

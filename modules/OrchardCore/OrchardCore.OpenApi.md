---
title: OpenApi
slug: OrchardCore.OpenApi
description:
  Microsoft.AspnetCore.OpenApi module for Orchard Core.
projectUrl: https://github.com/OrchardCMS/OrchardCore/tree/main/src/OrchardCore.Modules/OrchardCore.OpenApi
documentationUrl: https://docs.orchardcore.net/en/latest/reference/modules/OpenApi/
nuGetPackageId: OrchardCore.OpenApi
tags: ["Orchard Core"]
author:
  name: The Orchard Core Team
  url: https://github.com/OrchardCMS
  imageUrl: https://avatars.githubusercontent.com/u/9933239
licenses: [BSD-3-Clause]
pubDatetime: 2026-08-12T12:00:00Z
features:
  - id: OrchardCore.OpenApi
    name: OpenApi
    description: "Microsoft.AspnetCore.OpenApi module for Orchard Core. Its manifest-backed feature ID is `OrchardCore.OpenApi`, and it is categorized as Api. No additional feature dependencies are listed for it in this catalog entry. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Api
  - id: OrchardCore.OpenApi.SwaggerUI
    name: OpenApi Swagger UI
    description: "Enables the Swagger UI interactive API explorer at ~/swagger. Its manifest-backed feature ID is `OrchardCore.OpenApi.SwaggerUI`, and it is categorized as Api. It depends on `OrchardCore.OpenApi`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Api
    dependencies:
      - OrchardCore.OpenApi
  - id: OrchardCore.OpenApi.ReDocUI
    name: OpenApi ReDoc UI
    description: "Enables the ReDoc read-only API documentation at ~/redoc. Its manifest-backed feature ID is `OrchardCore.OpenApi.ReDocUI`, and it is categorized as Api. It depends on `OrchardCore.OpenApi`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Api
    dependencies:
      - OrchardCore.OpenApi
  - id: OrchardCore.OpenApi.ScalarUI
    name: OpenApi Scalar UI
    description: "Enables the Scalar modern API reference at ~/scalar/v1. Its manifest-backed feature ID is `OrchardCore.OpenApi.ScalarUI`, and it is categorized as Api. It depends on `OrchardCore.OpenApi`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Api
    dependencies:
      - OrchardCore.OpenApi
---
Microsoft.AspnetCore.OpenApi module for Orchard Core.

## Features

### OpenApi

Microsoft.AspnetCore.OpenApi module for Orchard Core. Its manifest-backed feature ID is `OrchardCore.OpenApi`, and it is categorized as Api. No additional feature dependencies are listed for it in this catalog entry. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### OpenApi Swagger UI

Enables the Swagger UI interactive API explorer at ~/swagger. Its manifest-backed feature ID is `OrchardCore.OpenApi.SwaggerUI`, and it is categorized as Api. It depends on `OrchardCore.OpenApi`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### OpenApi ReDoc UI

Enables the ReDoc read-only API documentation at ~/redoc. Its manifest-backed feature ID is `OrchardCore.OpenApi.ReDocUI`, and it is categorized as Api. It depends on `OrchardCore.OpenApi`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### OpenApi Scalar UI

Enables the Scalar modern API reference at ~/scalar/v1. Its manifest-backed feature ID is `OrchardCore.OpenApi.ScalarUI`, and it is categorized as Api. It depends on `OrchardCore.OpenApi`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

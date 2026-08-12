---
title: Redis
slug: OrchardCore.Redis
description:
  Redis configuration support.
projectUrl: https://github.com/OrchardCMS/OrchardCore/tree/main/src/OrchardCore.Modules/OrchardCore.Redis
documentationUrl: https://docs.orchardcore.net/en/latest/reference/modules/Redis/
nuGetPackageId: OrchardCore.Redis
tags: ["Orchard Core"]
author:
  name: The Orchard Core Team
  url: https://github.com/OrchardCMS
  imageUrl: https://avatars.githubusercontent.com/u/9933239
licenses: [BSD-3-Clause]
pubDatetime: 2026-08-12T12:00:00Z
features:
  - id: OrchardCore.Redis
    name: Redis
    description: "Redis configuration support. Its manifest-backed feature ID is `OrchardCore.Redis`, and it is categorized as Distributed. No additional feature dependencies are listed for it in this catalog entry. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Distributed
  - id: OrchardCore.Redis.Cache
    name: Redis Cache
    description: "Distributed cache using Redis. Its manifest-backed feature ID is `OrchardCore.Redis.Cache`, and it is categorized as Distributed. It depends on `OrchardCore.Redis`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Distributed
    dependencies:
      - OrchardCore.Redis
  - id: OrchardCore.Redis.Bus
    name: Redis Bus
    description: "Makes the Signal service distributed. Its manifest-backed feature ID is `OrchardCore.Redis.Bus`, and it is categorized as Distributed. It depends on `OrchardCore.Redis`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Distributed
    dependencies:
      - OrchardCore.Redis
  - id: OrchardCore.Redis.Lock
    name: Redis Lock
    description: "Distributed Lock using Redis. Its manifest-backed feature ID is `OrchardCore.Redis.Lock`, and it is categorized as Distributed. It depends on `OrchardCore.Redis`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Distributed
    dependencies:
      - OrchardCore.Redis
  - id: OrchardCore.Redis.DataProtection
    name: Distributed Data Protection (Redis)
    description: "Enables distributed data protection using Redis; recommended only with a Redis server configured for persistence. Its manifest-backed feature ID is `OrchardCore.Redis.DataProtection`, and it is categorized as Security. It depends on `OrchardCore.Redis`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Security
    dependencies:
      - OrchardCore.Redis
---
Redis configuration support.

## Features

### Redis

Redis configuration support. Its manifest-backed feature ID is `OrchardCore.Redis`, and it is categorized as Distributed. No additional feature dependencies are listed for it in this catalog entry. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Redis Cache

Distributed cache using Redis. Its manifest-backed feature ID is `OrchardCore.Redis.Cache`, and it is categorized as Distributed. It depends on `OrchardCore.Redis`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Redis Bus

Makes the Signal service distributed. Its manifest-backed feature ID is `OrchardCore.Redis.Bus`, and it is categorized as Distributed. It depends on `OrchardCore.Redis`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Redis Lock

Distributed Lock using Redis. Its manifest-backed feature ID is `OrchardCore.Redis.Lock`, and it is categorized as Distributed. It depends on `OrchardCore.Redis`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Distributed Data Protection (Redis)

Enables distributed data protection using Redis; recommended only with a Redis server configured for persistence. Its manifest-backed feature ID is `OrchardCore.Redis.DataProtection`, and it is categorized as Security. It depends on `OrchardCore.Redis`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

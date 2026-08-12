---
title: "Garnet"
slug: OrchardCoreContrib.Garnet
description:
  Provides Garnet features for configuration, cache, bus and data protection. It helps Orchard Core sites add
  this community-maintained capability while exposing package, dependency, source, and documentation details in
  the extensions gallery.
projectUrl: https://github.com/OrchardCoreContrib/OrchardCoreContrib.Modules/blob/main/src/OrchardCoreContrib.Garnet/README.md
documentationUrl: https://github.com/OrchardCoreContrib/OrchardCoreContrib.Modules/blob/main/src/OrchardCoreContrib.Garnet/README.md
nuGetPackageId: OrchardCoreContrib.Garnet
tags: ["Orchard Core", "Garnet", "Caching", "Distributed Caching", "Data Protection"]
author:
  name: OrchardCoreContrib
  url: https://github.com/OrchardCoreContrib
  imageUrl: https://avatars.githubusercontent.com/u/65380704
licenses: [BSD-3-Clause]
pubDatetime: 2026-07-17T18:28:09Z
features:
  - id: OrchardCoreContrib.Garnet
    name: "Garnet"
    description: "Garnet configuration support. Its upstream feature ID is `OrchardCoreContrib.Garnet`, and it is categorized as Distributed Caching. No additional feature dependencies are listed for it in the upstream manifest. This description is based on the OrchardCoreContrib manifest metadata; Orchard Core displays feature entries in the feature management UI with their description, category, and dependencies."
    category: "Distributed Caching"
  - id: OrchardCoreContrib.Garnet.Cache
    name: "Garnet Cache"
    description: "Distributed cache using Garnet. Its upstream feature ID is `OrchardCoreContrib.Garnet.Cache`, and it is categorized as Distributed Caching. It depends on `OrchardCoreContrib.Garnet`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the OrchardCoreContrib manifest metadata; Orchard Core displays feature entries in the feature management UI with their description, category, and dependencies."
    category: "Distributed Caching"
    dependencies:
      - OrchardCoreContrib.Garnet
  - id: OrchardCoreContrib.Garnet.Bus
    name: "Garnet Bus"
    description: "Makes the Signal service distributed though Garnet. Its upstream feature ID is `OrchardCoreContrib.Garnet.Bus`, and it is categorized as Distributed Caching. It depends on `OrchardCoreContrib.Garnet`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the OrchardCoreContrib manifest metadata; Orchard Core displays feature entries in the feature management UI with their description, category, and dependencies."
    category: "Distributed Caching"
    dependencies:
      - OrchardCoreContrib.Garnet
  - id: OrchardCoreContrib.Garnet.DataProtection
    name: "Garnet DataProtection"
    description: "Distributed DataProtection using Garnet. Its upstream feature ID is `OrchardCoreContrib.Garnet.DataProtection`, and it is categorized as Distributed Caching. It depends on `OrchardCoreContrib.Garnet`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the OrchardCoreContrib manifest metadata; Orchard Core displays feature entries in the feature management UI with their description, category, and dependencies."
    category: "Distributed Caching"
    dependencies:
      - OrchardCoreContrib.Garnet
  - id: OrchardCoreContrib.Garnet.Lock
    name: "Garnet Lock"
    description: "Distributed Lock using Garnet. Its upstream feature ID is `OrchardCoreContrib.Garnet.Lock`, and it is categorized as Distributed Caching. It depends on `OrchardCoreContrib.Garnet`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the OrchardCoreContrib manifest metadata; Orchard Core displays feature entries in the feature management UI with their description, category, and dependencies."
    category: "Distributed Caching"
    dependencies:
      - OrchardCoreContrib.Garnet
---
Provides Garnet features for configuration, cache, bus and data protection.

## Features

### Garnet

Garnet configuration support. Its upstream feature ID is `OrchardCoreContrib.Garnet`, and it is categorized as Distributed Caching. No additional feature dependencies are listed for it in the upstream manifest. This description is based on the OrchardCoreContrib manifest metadata; Orchard Core displays feature entries in the feature management UI with their description, category, and dependencies.

### Garnet Cache

Distributed cache using Garnet. Its upstream feature ID is `OrchardCoreContrib.Garnet.Cache`, and it is categorized as Distributed Caching. It depends on `OrchardCoreContrib.Garnet`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the OrchardCoreContrib manifest metadata; Orchard Core displays feature entries in the feature management UI with their description, category, and dependencies.

### Garnet Bus

Makes the Signal service distributed though Garnet. Its upstream feature ID is `OrchardCoreContrib.Garnet.Bus`, and it is categorized as Distributed Caching. It depends on `OrchardCoreContrib.Garnet`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the OrchardCoreContrib manifest metadata; Orchard Core displays feature entries in the feature management UI with their description, category, and dependencies.

### Garnet DataProtection

Distributed DataProtection using Garnet. Its upstream feature ID is `OrchardCoreContrib.Garnet.DataProtection`, and it is categorized as Distributed Caching. It depends on `OrchardCoreContrib.Garnet`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the OrchardCoreContrib manifest metadata; Orchard Core displays feature entries in the feature management UI with their description, category, and dependencies.

### Garnet Lock

Distributed Lock using Garnet. Its upstream feature ID is `OrchardCoreContrib.Garnet.Lock`, and it is categorized as Distributed Caching. It depends on `OrchardCoreContrib.Garnet`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the OrchardCoreContrib manifest metadata; Orchard Core displays feature entries in the feature management UI with their description, category, and dependencies.

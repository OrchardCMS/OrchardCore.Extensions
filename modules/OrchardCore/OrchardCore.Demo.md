---
title: Orchard Demo
slug: OrchardCore.Demo
description:
  Orchard Demo provides sample Orchard Core features for testing and demonstrating module behavior. It includes
  Orchard Demo and Orchard Foo Demo features in the Samples area, making the package easier to find when
  browsing related Orchard Core capabilities, dependencies, and documentation.
projectUrl: https://github.com/OrchardCMS/OrchardCore/tree/main/src/OrchardCore.Modules/OrchardCore.Demo
documentationUrl: https://docs.orchardcore.net/en/latest/reference/modules/Demo/
nuGetPackageId: OrchardCore.Demo
tags: ["Orchard Core"]
author:
  name: The Orchard Core Team
  url: https://docs.orchardcore.net
  imageUrl: https://docs.orchardcore.net/en/latest/assets/images/orchard-logo.png
licenses: [BSD-3-Clause]
pubDatetime: 2026-08-12T12:00:00Z
features:
  - id: OrchardCore.Demo
    name: Orchard Demo
    description: "Test. Its manifest-backed feature ID is `OrchardCore.Demo`, and it is categorized as Samples. It depends on `OrchardCore.Users`, and `OrchardCore.Contents`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Samples
    dependencies:
      - OrchardCore.Users
      - OrchardCore.Contents
  - id: OrchardCore.Demo.Foo
    name: Orchard Foo Demo
    description: "Foo feature sample. Its manifest-backed feature ID is `OrchardCore.Demo.Foo`, and it is categorized as Samples. No additional feature dependencies are listed for it in this catalog entry. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Samples
---
Test

## Features

### Orchard Demo

Test. Its manifest-backed feature ID is `OrchardCore.Demo`, and it is categorized as Samples. It depends on `OrchardCore.Users`, and `OrchardCore.Contents`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Orchard Foo Demo

Foo feature sample. Its manifest-backed feature ID is `OrchardCore.Demo.Foo`, and it is categorized as Samples. No additional feature dependencies are listed for it in this catalog entry. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

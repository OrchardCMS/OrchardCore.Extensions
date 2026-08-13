---
title: XML-RPC
slug: OrchardCore.XmlRpc
description:
  The XML-RPC module enables creation of contents from client applications such as Open Live Writer. It includes
  XML-RPC and Remote Publishing features in the Infrastructure area, making the package easier to find when
  browsing related Orchard Core capabilities, dependencies, and documentation.
projectUrl: https://github.com/OrchardCMS/OrchardCore/tree/main/src/OrchardCore.Modules/OrchardCore.XmlRpc
documentationUrl: https://docs.orchardcore.net
nuGetPackageId: OrchardCore.XmlRpc
tags: ["Orchard Core"]
author:
  name: The Orchard Core Team
  url: https://docs.orchardcore.net
  imageUrl: https://docs.orchardcore.net/en/latest/assets/images/favicon.png
licenses: [BSD-3-Clause]
compatibleWithAllVersions: true
pubDatetime: 2026-08-12T12:00:00Z
features:
  - id: OrchardCore.XmlRpc
    name: XML-RPC
    description: "The XML-RPC module enables creation of contents from client applications such as Open Live Writer. Its manifest-backed feature ID is `OrchardCore.XmlRpc`, and it is categorized as Infrastructure. No additional feature dependencies are listed for it in this catalog entry. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Infrastructure
  - id: OrchardCore.RemotePublishing
    name: Remote Publishing
    description: "The remote publishing feature enables creation of contents from client applications such as Open Live Writer. Its manifest-backed feature ID is `OrchardCore.RemotePublishing`, and it is categorized as Infrastructure. It depends on `OrchardCore.XmlRpc`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Infrastructure
    dependencies:
      - OrchardCore.XmlRpc
---
The XML-RPC module enables creation of contents from client applications such as Open Live Writer.

## Features

### XML-RPC

The XML-RPC module enables creation of contents from client applications such as Open Live Writer. Its manifest-backed feature ID is `OrchardCore.XmlRpc`, and it is categorized as Infrastructure. No additional feature dependencies are listed for it in this catalog entry. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Remote Publishing

The remote publishing feature enables creation of contents from client applications such as Open Live Writer. Its manifest-backed feature ID is `OrchardCore.RemotePublishing`, and it is categorized as Infrastructure. It depends on `OrchardCore.XmlRpc`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

---
title: Contents
slug: OrchardCore.Contents
description:
  The contents module enables the edition and rendering of content items. It includes Contents, Content Version
  Pruning and related features in the Content Management area, making the package easier to find when browsing
  related Orchard Core capabilities, dependencies, and documentation.
projectUrl: https://github.com/OrchardCMS/OrchardCore/tree/main/src/OrchardCore.Modules/OrchardCore.Contents
documentationUrl: https://docs.orchardcore.net/en/latest/reference/modules/Contents/
nuGetPackageId: OrchardCore.Contents
tags: ["Orchard Core"]
author:
  name: The Orchard Core Team
  url: https://docs.orchardcore.net
  imageUrl: https://docs.orchardcore.net/en/latest/assets/images/orchard-logo.png
licenses: [BSD-3-Clause]
pubDatetime: 2026-08-12T12:00:00Z
features:
  - id: OrchardCore.Contents
    name: Contents
    description: "The contents module enables the edition and rendering of content items. Its manifest-backed feature ID is `OrchardCore.Contents`, and it is categorized as Content Management. It depends on `OrchardCore.Settings`, and `OrchardCore.Liquid`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Content Management
    dependencies:
      - OrchardCore.Settings
      - OrchardCore.Liquid
  - id: OrchardCore.Contents.VersionPruning
    name: Content Version Pruning
    description: "Provides a background task to prune old content item versions. Its manifest-backed feature ID is `OrchardCore.Contents.VersionPruning`, and it is categorized as Content Management. It depends on `OrchardCore.Contents`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Content Management
    dependencies:
      - OrchardCore.Contents
  - id: OrchardCore.Contents.FileContentDefinition
    name: File Content Definition
    description: "Stores Content Definition in a local file. Its manifest-backed feature ID is `OrchardCore.Contents.FileContentDefinition`, and it is categorized as Content Management. It depends on `OrchardCore.Contents`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Content Management
    dependencies:
      - OrchardCore.Contents
  - id: OrchardCore.Contents.Deployment.ExportContentToDeploymentTarget
    name: Export Content To Deployment Target
    description: "Adds an export to deployment target action to the content items list. Its manifest-backed feature ID is `OrchardCore.Contents.Deployment.ExportContentToDeploymentTarget`, and it is categorized as Content Management. It depends on `OrchardCore.Contents`, `OrchardCore.Deployment`, and `OrchardCore.Recipes.Core`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Content Management
    dependencies:
      - OrchardCore.Contents
      - OrchardCore.Deployment
      - OrchardCore.Recipes.Core
  - id: OrchardCore.Contents.Deployment.AddToDeploymentPlan
    name: Add Content To Deployment Plan
    description: "Adds an add to deployment plan action to the content items list. Its manifest-backed feature ID is `OrchardCore.Contents.Deployment.AddToDeploymentPlan`, and it is categorized as Content Management. It depends on `OrchardCore.Contents`, and `OrchardCore.Deployment`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Content Management
    dependencies:
      - OrchardCore.Contents
      - OrchardCore.Deployment
  - id: OrchardCore.Contents.Deployment.Download
    name: View Or Download Content As JSON
    description: "View or download content as JSON from the content items list. Its manifest-backed feature ID is `OrchardCore.Contents.Deployment.Download`, and it is categorized as Content Management. It depends on `OrchardCore.Contents`, and `OrchardCore.Deployment`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Content Management
    dependencies:
      - OrchardCore.Contents
      - OrchardCore.Deployment
---
The contents module enables the edition and rendering of content items.

## Features

### Contents

The contents module enables the edition and rendering of content items. Its manifest-backed feature ID is `OrchardCore.Contents`, and it is categorized as Content Management. It depends on `OrchardCore.Settings`, and `OrchardCore.Liquid`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Content Version Pruning

Provides a background task to prune old content item versions. Its manifest-backed feature ID is `OrchardCore.Contents.VersionPruning`, and it is categorized as Content Management. It depends on `OrchardCore.Contents`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### File Content Definition

Stores Content Definition in a local file. Its manifest-backed feature ID is `OrchardCore.Contents.FileContentDefinition`, and it is categorized as Content Management. It depends on `OrchardCore.Contents`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Export Content To Deployment Target

Adds an export to deployment target action to the content items list. Its manifest-backed feature ID is `OrchardCore.Contents.Deployment.ExportContentToDeploymentTarget`, and it is categorized as Content Management. It depends on `OrchardCore.Contents`, `OrchardCore.Deployment`, and `OrchardCore.Recipes.Core`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Add Content To Deployment Plan

Adds an add to deployment plan action to the content items list. Its manifest-backed feature ID is `OrchardCore.Contents.Deployment.AddToDeploymentPlan`, and it is categorized as Content Management. It depends on `OrchardCore.Contents`, and `OrchardCore.Deployment`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### View Or Download Content As JSON

View or download content as JSON from the content items list. Its manifest-backed feature ID is `OrchardCore.Contents.Deployment.Download`, and it is categorized as Content Management. It depends on `OrchardCore.Contents`, and `OrchardCore.Deployment`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

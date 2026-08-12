---
title: "Orchard Core Contrib - Health Checks"
slug: OrchardCoreContrib.HealthChecks
description:
  Provides health checks for your website. It helps Orchard Core sites add this community-maintained capability
  while exposing package, dependency, source, and documentation details in the extensions gallery.
projectUrl: https://github.com/OrchardCoreContrib/OrchardCoreContrib.Modules/blob/main/src/OrchardCoreContrib.HealthChecks/README.md
documentationUrl: https://github.com/OrchardCoreContrib/OrchardCoreContrib.Modules/blob/main/src/OrchardCoreContrib.HealthChecks/README.md
nuGetPackageId: OrchardCoreContrib.HealthChecks
tags: ["Orchard Core", "Health Checks"]
author:
  name: OrchardCoreContrib
  url: https://github.com/OrchardCoreContrib
  imageUrl: https://avatars.githubusercontent.com/u/65380704
licenses: [BSD-3-Clause]
pubDatetime: 2026-07-17T18:28:09Z
features:
  - id: OrchardCoreContrib.HealthChecks
    name: "Health Checks"
    description: "Provides health checks for the website. Its upstream feature ID is `OrchardCoreContrib.HealthChecks`, and it is categorized as Health Checks. No additional feature dependencies are listed for it in the upstream manifest. This description is based on the OrchardCoreContrib manifest metadata; Orchard Core displays feature entries in the feature management UI with their description, category, and dependencies."
    category: "Health Checks"
  - id: OrchardCoreContrib.HealthChecks.IPRestriction
    name: "Health Checks IP Restriction"
    description: "Restricts access to health checks endpoints by IP address. Its upstream feature ID is `OrchardCoreContrib.HealthChecks.IPRestriction`, and it is categorized as Health Checks. It depends on `OrchardCoreContrib.HealthChecks`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the OrchardCoreContrib manifest metadata; Orchard Core displays feature entries in the feature management UI with their description, category, and dependencies."
    category: "Health Checks"
    dependencies:
      - OrchardCoreContrib.HealthChecks
  - id: OrchardCoreContrib.HealthChecks.RateLimiting
    name: "Health Checks Rate Limiting"
    description: "Limits requests to health checks endpoints to prevent DOS attacks. Its upstream feature ID is `OrchardCoreContrib.HealthChecks.RateLimiting`, and it is categorized as Health Checks. It depends on `OrchardCoreContrib.HealthChecks`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the OrchardCoreContrib manifest metadata; Orchard Core displays feature entries in the feature management UI with their description, category, and dependencies."
    category: "Health Checks"
    dependencies:
      - OrchardCoreContrib.HealthChecks
  - id: OrchardCoreContrib.HealthChecks.BlockingRateLimiting
    name: "Health Checks Blocking Rate Limiting"
    description: "Adds blocking behavior to the health checks rate limiter. Clients exceeding the limit are temporarily blocked to prevent DoS attacks. Its upstream feature ID is `OrchardCoreContrib.HealthChecks.BlockingRateLimiting`, and it is categorized as Health Checks. It depends on `OrchardCoreContrib.HealthChecks.RateLimiting`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the OrchardCoreContrib manifest metadata; Orchard Core displays feature entries in the feature management UI with their description, category, and dependencies."
    category: "Health Checks"
    dependencies:
      - OrchardCoreContrib.HealthChecks.RateLimiting
---
Provides health checks for your website.

## Features

### Health Checks

Provides health checks for the website. Its upstream feature ID is `OrchardCoreContrib.HealthChecks`, and it is categorized as Health Checks. No additional feature dependencies are listed for it in the upstream manifest. This description is based on the OrchardCoreContrib manifest metadata; Orchard Core displays feature entries in the feature management UI with their description, category, and dependencies.

### Health Checks IP Restriction

Restricts access to health checks endpoints by IP address. Its upstream feature ID is `OrchardCoreContrib.HealthChecks.IPRestriction`, and it is categorized as Health Checks. It depends on `OrchardCoreContrib.HealthChecks`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the OrchardCoreContrib manifest metadata; Orchard Core displays feature entries in the feature management UI with their description, category, and dependencies.

### Health Checks Rate Limiting

Limits requests to health checks endpoints to prevent DOS attacks. Its upstream feature ID is `OrchardCoreContrib.HealthChecks.RateLimiting`, and it is categorized as Health Checks. It depends on `OrchardCoreContrib.HealthChecks`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the OrchardCoreContrib manifest metadata; Orchard Core displays feature entries in the feature management UI with their description, category, and dependencies.

### Health Checks Blocking Rate Limiting

Adds blocking behavior to the health checks rate limiter. Clients exceeding the limit are temporarily blocked to prevent DoS attacks. Its upstream feature ID is `OrchardCoreContrib.HealthChecks.BlockingRateLimiting`, and it is categorized as Health Checks. It depends on `OrchardCoreContrib.HealthChecks.RateLimiting`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the OrchardCoreContrib manifest metadata; Orchard Core displays feature entries in the feature management UI with their description, category, and dependencies.

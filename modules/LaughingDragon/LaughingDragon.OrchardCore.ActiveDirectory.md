---
title: "Tor (Active Directory sign-in)"
description: "Active Directory sign-in for Orchard Core over LDAPS. It binds as the signing-in user: no service account and no stored directory password."
dependencies: ["OrchardCore.Users", "OrchardCore.Roles", "OrchardCore.Users.CustomUserSettings", "OrchardCore.Media"]
projectUrl: https://github.com/LaughingDragon/Tor-AD-Authentication
documentationUrl: https://github.com/LaughingDragon/Tor-AD-Authentication#readme
nuGetPackageId: LaughingDragon.OrchardCore.ActiveDirectory
tags:
  - active-directory
  - ldap
  - ldaps
  - authentication
  - security
author:
  name: Liam P. Ward
  url: https://github.com/LaughingDragon
  imageUrl: https://avatars.githubusercontent.com/u/25347681
licenses: [MIT]
versions:
  - 3.0.1
pubDatetime: 2026-11-25T22:38:18Z
---

Tor lets Active Directory domain accounts sign in on Orchard Core's own login page. A companion feature, **Tor Account**, gives each signed-in user an account page at `/account` for their own directory details, domain password, domain picture and contact details.

- **Binds as the user.** Tor takes the name and password typed on Orchard's login form and binds to the domain controllers over LDAPS with them. There is no service account, and Tor stores no directory password.
- **Group gate and managed roles.** Access is limited to members of the groups you map to Orchard roles. The map is empty by default, so no directory account can sign in until you configure it. Mapping a group to Administrator is refused unless you allow it explicitly.
- **Follows Orchard's login.** Orchard's own login events and account checks run for directory sign-ins. Failures are throttled, logged and answered identically, and unexpected errors fail closed.
- **Break-glass accounts.** Local Orchard accounts named in configuration keep signing in through Orchard's own login.

**Status: stable (1.0.0).** A line-by-line security review has been done and its fixes are in this release. The remaining risks are listed in the threat model in the repository. Within 1.x, setting keys, defaults, feature ids and permission names only change in a major version, and the repository documents every setting. This release has been verified on one production site, against Orchard Core 3.0.1 on .NET 10, and has not yet been run against a second directory, so reports from other domains are welcome. Please report vulnerabilities through GitHub's private vulnerability reporting rather than a public issue.

**Limitations.** Directory users who have two-factor authentication turned on or required in Orchard are refused. The sign-in never says why it failed. Domain controllers must be reachable over LDAPS.

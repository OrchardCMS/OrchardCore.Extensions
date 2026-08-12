---
title: Users
slug: OrchardCore.Users
description:
  The users module enables authentication UI and user management. It includes Users, External Authentication and
  related features in the Security and Settings area, making the package easier to find when browsing related
  Orchard Core capabilities, dependencies, and documentation.
projectUrl: https://github.com/OrchardCMS/OrchardCore/tree/main/src/OrchardCore.Modules/OrchardCore.Users
documentationUrl: https://docs.orchardcore.net/en/latest/reference/modules/Users/
nuGetPackageId: OrchardCore.Users
tags: ["Orchard Core"]
author:
  name: The Orchard Core Team
  url: https://docs.orchardcore.net
  imageUrl: https://docs.orchardcore.net/en/latest/assets/images/favicon.png
licenses: [BSD-3-Clause]
pubDatetime: 2026-08-12T12:00:00Z
features:
  - id: OrchardCore.Users
    name: Users
    description: "The users module enables authentication UI and user management. Its manifest-backed feature ID is `OrchardCore.Users`, and it is categorized as Security. It depends on `OrchardCore.Roles.Core`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Security
    dependencies:
      - OrchardCore.Roles.Core
  - id: OrchardCore.Users.ExternalAuthentication
    name: External Authentication
    description: "Provides a way to allow authentication using an external identity provider. Its manifest-backed feature ID is `OrchardCore.Users.ExternalAuthentication`, and it is categorized as Security. It depends on `OrchardCore.Users`, so Orchard Core enables that dependency when this feature is enabled. The manifest marks it as enabled by dependency only, so it is intended to support other features rather than be selected as a standalone end-user feature. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Security
    dependencies:
      - OrchardCore.Users
    enabledByDependencyOnly: true
  - id: OrchardCore.Users.ChangeEmail
    name: Users Change Email
    description: "The Change email feature allows users to change their email address. Its manifest-backed feature ID is `OrchardCore.Users.ChangeEmail`, and it is categorized as Security. It depends on `OrchardCore.Users`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Security
    dependencies:
      - OrchardCore.Users
  - id: OrchardCore.Users.Registration
    name: Users Registration
    description: "The registration feature allows external users to sign up to the site and ask to confirm their email. Its manifest-backed feature ID is `OrchardCore.Users.Registration`, and it is categorized as Security. It depends on `OrchardCore.Users`, and `OrchardCore.Email`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Security
    dependencies:
      - OrchardCore.Users
      - OrchardCore.Email
  - id: OrchardCore.Users.ResetPassword
    name: Users Reset Password
    description: "The reset password feature allows users to reset their password. Its manifest-backed feature ID is `OrchardCore.Users.ResetPassword`, and it is categorized as Security. It depends on `OrchardCore.Users`, and `OrchardCore.Email`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Security
    dependencies:
      - OrchardCore.Users
      - OrchardCore.Email
  - id: OrchardCore.Users.TimeZone
    name: User Time Zone
    description: "Provides a way to set the time zone per user. Its manifest-backed feature ID is `OrchardCore.Users.TimeZone`, and it is categorized as Settings. It depends on `OrchardCore.Users`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Settings
    dependencies:
      - OrchardCore.Users
  - id: OrchardCore.Users.Localization
    name: User Localization
    description: "Provides a way to set the culture per user. Its manifest-backed feature ID is `OrchardCore.Users.Localization`, and it is categorized as Settings. It depends on `OrchardCore.Users`, and `OrchardCore.Localization`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Settings
    dependencies:
      - OrchardCore.Users
      - OrchardCore.Localization
  - id: OrchardCore.Users.CustomUserSettings
    name: Custom User Settings
    description: "The custom user settings feature allows content types to become custom user settings. Its manifest-backed feature ID is `OrchardCore.Users.CustomUserSettings`, and it is categorized as Settings. It depends on `OrchardCore.Users`, and `OrchardCore.Contents`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Settings
    dependencies:
      - OrchardCore.Users
      - OrchardCore.Contents
  - id: OrchardCore.Users.AuditTrail
    name: Users Audit Trail
    description: "The users audit trail feature allows logging of user events. Its manifest-backed feature ID is `OrchardCore.Users.AuditTrail`, and it is categorized as Security. It depends on `OrchardCore.Users`, and `OrchardCore.AuditTrail`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Security
    dependencies:
      - OrchardCore.Users
      - OrchardCore.AuditTrail
  - id: OrchardCore.Users.Authentication.CacheTicketStore
    name: Users Authentication Ticket Store
    description: "Stores users authentication tickets on server in memory cache instead of cookies. If distributed cache feature is enabled it will store authentication tickets on distributed cache. Its manifest-backed feature ID is `OrchardCore.Users.Authentication.CacheTicketStore`, and it is categorized as Security. It depends on `OrchardCore.Users`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Security
    dependencies:
      - OrchardCore.Users
  - id: OrchardCore.Users.2FA
    name: Two-Factor Authentication Services
    description: "Provides Two-factor core services. Its manifest-backed feature ID is `OrchardCore.Users.2FA`, and it is categorized as Security. It depends on `OrchardCore.Users`, so Orchard Core enables that dependency when this feature is enabled. The manifest marks it as enabled by dependency only, so it is intended to support other features rather than be selected as a standalone end-user feature. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Security
    dependencies:
      - OrchardCore.Users
    enabledByDependencyOnly: true
  - id: OrchardCore.Users.2FA.AuthenticatorApp
    name: Two-Factor Authenticator App Method
    description: "Provides users a two-factor authentication method through any Authentication App. Its manifest-backed feature ID is `OrchardCore.Users.2FA.AuthenticatorApp`, and it is categorized as Security. It depends on `OrchardCore.Users`, and `OrchardCore.Users.2FA`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Security
    dependencies:
      - OrchardCore.Users
      - OrchardCore.Users.2FA
  - id: OrchardCore.Users.2FA.Email
    name: Two-Factor Email Method
    description: "Provides users a two-factor authentication method through an Email service. Its manifest-backed feature ID is `OrchardCore.Users.2FA.Email`, and it is categorized as Security. It depends on `OrchardCore.Users`, `OrchardCore.Users.2FA`, `OrchardCore.Liquid`, and `OrchardCore.Email`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Security
    dependencies:
      - OrchardCore.Users
      - OrchardCore.Users.2FA
      - OrchardCore.Liquid
      - OrchardCore.Email
  - id: OrchardCore.Users.2FA.Sms
    name: Two-Factor SMS Method
    description: "Provides users a two-factor authentication method through an SMS service. Its manifest-backed feature ID is `OrchardCore.Users.2FA.Sms`, and it is categorized as Security. It depends on `OrchardCore.Users`, `OrchardCore.Users.2FA`, `OrchardCore.Liquid`, and `OrchardCore.Sms`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies."
    category: Security
    dependencies:
      - OrchardCore.Users
      - OrchardCore.Users.2FA
      - OrchardCore.Liquid
      - OrchardCore.Sms
---
The users module enables authentication UI and user management.

## Features

### Users

The users module enables authentication UI and user management. Its manifest-backed feature ID is `OrchardCore.Users`, and it is categorized as Security. It depends on `OrchardCore.Roles.Core`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### External Authentication

Provides a way to allow authentication using an external identity provider. Its manifest-backed feature ID is `OrchardCore.Users.ExternalAuthentication`, and it is categorized as Security. It depends on `OrchardCore.Users`, so Orchard Core enables that dependency when this feature is enabled. The manifest marks it as enabled by dependency only, so it is intended to support other features rather than be selected as a standalone end-user feature. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Users Change Email

The Change email feature allows users to change their email address. Its manifest-backed feature ID is `OrchardCore.Users.ChangeEmail`, and it is categorized as Security. It depends on `OrchardCore.Users`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Users Registration

The registration feature allows external users to sign up to the site and ask to confirm their email. Its manifest-backed feature ID is `OrchardCore.Users.Registration`, and it is categorized as Security. It depends on `OrchardCore.Users`, and `OrchardCore.Email`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Users Reset Password

The reset password feature allows users to reset their password. Its manifest-backed feature ID is `OrchardCore.Users.ResetPassword`, and it is categorized as Security. It depends on `OrchardCore.Users`, and `OrchardCore.Email`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### User Time Zone

Provides a way to set the time zone per user. Its manifest-backed feature ID is `OrchardCore.Users.TimeZone`, and it is categorized as Settings. It depends on `OrchardCore.Users`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### User Localization

Provides a way to set the culture per user. Its manifest-backed feature ID is `OrchardCore.Users.Localization`, and it is categorized as Settings. It depends on `OrchardCore.Users`, and `OrchardCore.Localization`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Custom User Settings

The custom user settings feature allows content types to become custom user settings. Its manifest-backed feature ID is `OrchardCore.Users.CustomUserSettings`, and it is categorized as Settings. It depends on `OrchardCore.Users`, and `OrchardCore.Contents`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Users Audit Trail

The users audit trail feature allows logging of user events. Its manifest-backed feature ID is `OrchardCore.Users.AuditTrail`, and it is categorized as Security. It depends on `OrchardCore.Users`, and `OrchardCore.AuditTrail`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Users Authentication Ticket Store

Stores users authentication tickets on server in memory cache instead of cookies. If distributed cache feature is enabled it will store authentication tickets on distributed cache. Its manifest-backed feature ID is `OrchardCore.Users.Authentication.CacheTicketStore`, and it is categorized as Security. It depends on `OrchardCore.Users`, so Orchard Core enables that dependency when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Two-Factor Authentication Services

Provides Two-factor core services. Its manifest-backed feature ID is `OrchardCore.Users.2FA`, and it is categorized as Security. It depends on `OrchardCore.Users`, so Orchard Core enables that dependency when this feature is enabled. The manifest marks it as enabled by dependency only, so it is intended to support other features rather than be selected as a standalone end-user feature. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Two-Factor Authenticator App Method

Provides users a two-factor authentication method through any Authentication App. Its manifest-backed feature ID is `OrchardCore.Users.2FA.AuthenticatorApp`, and it is categorized as Security. It depends on `OrchardCore.Users`, and `OrchardCore.Users.2FA`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Two-Factor Email Method

Provides users a two-factor authentication method through an Email service. Its manifest-backed feature ID is `OrchardCore.Users.2FA.Email`, and it is categorized as Security. It depends on `OrchardCore.Users`, `OrchardCore.Users.2FA`, `OrchardCore.Liquid`, and `OrchardCore.Email`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

### Two-Factor SMS Method

Provides users a two-factor authentication method through an SMS service. Its manifest-backed feature ID is `OrchardCore.Users.2FA.Sms`, and it is categorized as Security. It depends on `OrchardCore.Users`, `OrchardCore.Users.2FA`, `OrchardCore.Liquid`, and `OrchardCore.Sms`, so Orchard Core enables those dependencies when this feature is enabled. This description is based on the Orchard Core manifest and official documentation; in Orchard Core, feature entries are shown in the feature management UI with their description, category, and dependencies.

---
title: Etch Fields
slug: Etch.OrchardCore.Fields
description:
  Collection of useful content fields for Orchard Core.
projectUrl: https://github.com/EtchUK/Etch.OrchardCore.Fields
nuGetPackageId: Etch.OrchardCore.Fields
tags:
  - fields
author:
  name: EtchUk
  url: https://github.com/EtchUk
  imageUrl: https://avatars.githubusercontent.com/u/4966219
licenses: [MIT]
pubDatetime: 2024-09-15T12:00:00Z
---

### Code

Content field providing a code editor (using [Ace](https://ace.c9.io/)) to add code as content, perfect for displaying code samples.

![Screen recording of code field](https://github.com/EtchUK/Etch.OrchardCore.Fields/blob/main/docs/demo-code-field.gif?raw=true)

### Colour

Colour field introduces an alternative to the `TextField` for editors to define a colour. This field can be configured with a colour palette, transparent or the ability to choose a custom colour.

### Dictionary

Provides content field for managing an arbitrary amount of names and associated values. Items will be displayed on the page as an unordered list with name/value.

### Eventbrite

Provides a content field that will fetch event data from Eventbrite and display it as an unordered list.

### Multi Select

Content field that has a collection of pre-configured options where content editors can choose multiple options that will be rendered in an unordered list.

### Query

Editors can choose from a drop down list of [queries](https://docs.orchardcore.net/en/dev/docs/reference/modules/Queries/).

### Render Alias

Allows editors to specify a content item by its alias to be rendered in a specified display type.

### Responsive Media

Replica of the media field, however the field can have responsive breakpoints configured, which will be used to display a responsive image via the `picture` element. Content editors can define specific images for particular breakpoints, otherwise a [dynamically resized image](https://orchardcore.readthedocs.io/en/latest/OrchardCore.Modules/OrchardCore.Media/README/#resize_url) will be used for the breakpoint.

### Values

Content editors can define an arbitary list of values with a user friendly editor experience. Values will be displayed on the page as an unordered list.
---
# page settings
breadcrumbs:
  - title:
      en: Home
      fr: Accueil
    link:
      en: /en
      fr: /fr
  - title:
      en: Library
      fr: Bibliothèque
    link:
      en: /en/library
      fr: /fr/bibliotheque
contentTitle: Component example # Need an override for bilingual title
created: 2020-01-31 # ISO date format YYYY-MM-DD
description-short: # max 80 characters long
  en: Short description of maximum 80 characters
  fr: Brève description de 80 caractères maximum
description-long:
  en: Long description over 80 characters. Lorem ipsum dolor sit amet, an est albucius deserunt. Ea nusquam assueverit vis, ex nec audiam expetenda disputationi. Vis eu etiam officiis, vel et hendrerit scribentur. Vocent sententiae argumentum qui.
  fr: Description longue de plus de 80 caractères. Lôrem ipsum dôlor sît âmèt, utînàm màluîsset qùi eu. Omnes iisqué nônûmés has ex. Usu ad sçriptà çommunè suscîpït. Cum ôportèat sénsibûs maiêstatïs àn, êt debet dôlor pœssit prœ àperirî.
lang: en
layout: component
permalink: en/library/components/component
permalink_fr: fr/bibliotheque/composantes/composante
stylesheets:
  - href: "/assets/css/alpha-beta-banner.css"
synonmyns:
  en: [atom, module, molecule, pattern, plugin]
  fr: [atôme, module, molécule, motif, plugiciel]

# technical sheet
atomisation: organism # atom, molecule, orgamism (component), template (page layout), page, style, practice (design pattern), behaviour
code:
  code-variants:
    - variant:
      - layout-option:
        - html-example: # encoded html code with content
            en: |
                &lt;html&gt;
                  &lt;head&gt;
                    &lt;title&gt;HTML is awesome&lt;/title&gt;
                  &lt;/head&gt;
                  &lt;body&gt;
                    &lt;p&gt;HTML is awesome&lt;/p&gt;
                  &lt;/body&gt;
                &lt;/html&gt;
            fr: |
                &lt;html&gt;
                  &lt;head&gt;
                    &lt;title&gt;Le HTML est génial&lt;/title&gt;
                  &lt;/head&gt;
                  &lt;body&gt;
                    &lt;p&gt;Le HTML est génial&lt;/p&gt;
                  &lt;/body&gt;
                &lt;/html&gt;
          html-layout: # encoded html code without content
            html: # empty or false if commented
            liquid: |
                &lt;html&gt;
                  &lt;head&gt;
                    &lt;title&gt;{{ page.title }}&lt;/title&gt;
                  &lt;/head&gt;
                  &lt;body&gt;
                    {{ content }}
                  &lt;/body&gt;
                &lt;/html&gt;
            mustache: # empty or false if commented
            twig: # empty or false if commented
            version:
          id:
          stylesheet:
            css: |
                p {
                  color: black;
                }
            scss: # empty or false if commented
            version: 1.0
            variables: # css-variables
          scripts:
            js:
            typescript: # empty or false if commented
            version:
          value:
        name: # wet4, wet5, React, Angular, etc.
        schema:
          sample:
          verions:
        json-ld:
configuration: # Table of all configuration settings available
  - option:
      en:
      fr:
    description:
      en:
      fr:
    how-to:
      en:
      fr:
design-variants: # empty or false if commented
  - img:
      alt:
        en:
        fr:
      link:
        en:
        fr:
    texttag:
      en:
      fr:
    title:
      en:
      fr:
design-variant-screenshots:
  - link:
    alt:
      en:
      fr:
design-kits: # empty or false if commented
  - title: Photoshop
    link: \#
design-spec:
  callouts: # list of all the numbered indicators on the screenshot
  - number:
    texttag: # Values can span multiple lines using |. Spanning multiple lines using a “Literal Block Scalar” | will include the newlines and any trailing spaces.
      en:
      fr:
    title:
      en:
      fr:
  screenshot: # link to image
    alt:
      en:
      fr:
    link:
layout-options:
  - option:
      en:
      fr:
name:
  en:
  fr:
rationale:
  a11y:
    audit:
    considerations:
    - texttag:
        en:
        fr:
  intro:
    en:
    fr:
  research:
    - intro:
        en:
        fr:
      texttag:
        en:
        fr:
      title:
        en:
        fr:
related: # empty or false if commented
  - title:
      en:
      fr:
    link:
      en:
      fr:
release-notes:
  - notes:
      en: Some notes that could be useful
      fr:
    progress:
      en: Beta # alpha, beta, stable
      fr: Béta
    updated: 2020-02-01 # ISO date format YYYY-MM-DD
    version: v0.0.2 # see guidelines for semantic versioning
  - notes:
      en: Some notes that could be useful
      fr:
    progress:
      en: Alpha # alpha, beta, stable
      fr: Alpha
    updated: 2020-01-01 # ISO date format YYYY-MM-DD
    version: v0.0.1 # see guidelines for semantic versioning
rendering: # non-encoded html code with content
  en:
  fr:
states:
usage: # do and dont associated with a pattern
  - do: # can add as many do as needed
      en:
      fr:
    dont: # can add as many dont as needed
      en:
      fr:
    texttag: # ?: can markdown be uesd in yaml notation. Yes with the `|`
      en:
      fr:
---

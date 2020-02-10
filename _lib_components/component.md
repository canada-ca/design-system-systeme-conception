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
  - title:
      en: Component
      fr: Composante
    link:
      en: /en/library/component
      fr: /fr/bibliotheque/composante
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
  - href: /assets/css/alpha-beta-banner.css
  - href: /assets/css/do-dont.css
synonmyns:
  en: [atom, module, molecule, pattern, plugin]
  fr: [atôme, module, molécule, motif, plugiciel]

# technical sheet
atomisation: organism # atom, molecule, orgamism (component), template (page layout), page, style, practice (design pattern), behaviour
code:
  code-variants:
    - variants:
      - layout-option:
        - iframe-src: # url for the encoded html code with content
            en: |
                &lt;component&gt;
                  &lt;p&gt;This component is awesome&lt;/p&gt;
                &lt;/component&gt;
            fr: |
                &lt;component&gt;
                  &lt;p&gt;Cette composante est géniale&lt;/p&gt;
                &lt;/component&gt;
          html-layout: # encoded html code without content
            html: # empty or false if commented
            liquid: |
                &lt;component&gt;
                  &lt;p&gt;{{ content }}&lt;/p&gt;
                &lt;/component&gt;
            mustache: # empty or false if commented
            twig: # empty or false if commented
            version:
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
design-variants:
design-kits: # empty or false if commented
  - title: Photoshop
    link: \#
design-spec:
  callouts: # list of all the numbered indicators on the screenshot
  - number: 1
    texttag: # Values can span multiple lines using |. Spanning multiple lines using a “Literal Block Scalar” | will include the newlines and any trailing spaces.
      en: |
        <h3>Title 1.1</h3>
        <ul>
          <li>Some text 1.1.1</li>
          <li>Some text 1.1.2</li>
        </ul>
        <h3>Title 1.2</h3>
        <ul>
          <li>Some text 1.2.1</li>
          <li>Some text 1.2.2</li>
          <li>Some text 1.2.3</li>
        </ul>
      fr: |
        <h3>Titre 1.1</h3>
        <ul>
          <li>Texte quelconque 1.1.1</li>
          <li>Texte quelconque 1.1.2</li>
        </ul>
        <h3>Titre 1.2</h3>
        <ul>
          <li>Texte quelconque 1.2.1</li>
          <li>Texte quelconque 1.2.2</li>
          <li>Texte quelconque 1.2.3</li>
        </ul>
    title:
      en: Big title 1
      fr: Gros titre 1
  - number: 2
    texttag:
      en: |
        <h3>Title 2.1</h3>
        <ul>
          <li>Some text 2.1.1</li>
          <li>Some text 2.1.2</li>
        </ul>
        <h3>Title 2.2</h3>
        <ul>
          <li>Some text 2.2.1</li>
          <li>Some text 2.2.2</li>
          <li>Some text 2.2.3</li>
        </ul>
      fr: |
        <h3>Titre 2.1</h3>
        <ul>
          <li>Texte quelconque 2.1.1</li>
          <li>Texte quelconque 2.1.2</li>
        </ul>
        <h3>Titre 2.2</h3>
        <ul>
          <li>Texte quelconque 2.2.1</li>
          <li>Texte quelconque 2.2.2</li>
          <li>Texte quelconque 2.2.3</li>
        </ul>
    title:
      en: Big title 2
      fr: Gros titre 2
  - number: 3
    texttag:
      en: |
        <h3>Title 3.1</h3>
        <ul>
          <li>Some text 3.1.1</li>
          <li>Some text 3.1.2</li>
        </ul>
        <h3>Title 3.2</h3>
        <ul>
          <li>Some text 3.2.1</li>
          <li>Some text 3.2.2</li>
          <li>Some text 3.2.3</li>
        </ul>
      fr: |
        <h3>Titre 3.1</h3>
        <ul>
          <li>Texte quelconque 3.1.1</li>
          <li>Texte quelconque 3.1.2</li>
        </ul>
        <h3>Titre 3.2</h3>
        <ul>
          <li>Texte quelconque 3.2.1</li>
          <li>Texte quelconque 3.2.2</li>
          <li>Texte quelconque 3.2.3</li>
        </ul>
    title:
      en: Big title 3
      fr: Gros titre 3
  - number: 4
    texttag:
      en: |
        <h3>Title 4.1</h3>
        <ul>
          <li>Some text 4.1.1</li>
          <li>Some text 4.1.2</li>
        </ul>
        <h3>Title 4.2</h3>
        <ul>
          <li>Some text 4.2.1</li>
          <li>Some text 4.2.2</li>
          <li>Some text 4.2.3</li>
        </ul>
      fr: |
        <h3>Titre 4.1</h3>
        <ul>
          <li>Texte quelconque 4.1.1</li>
          <li>Texte quelconque 4.1.2</li>
        </ul>
        <h3>Titre 4.2</h3>
        <ul>
          <li>Texte quelconque 4.2.1</li>
          <li>Texte quelconque 4.2.2</li>
          <li>Texte quelconque 4.2.3</li>
        </ul>
    title:
      en: Big title 4
      fr: Gros titre 4
  - number: 5
    texttag:
      en: |
        <h3>Title 5.1</h3>
        <ul>
          <li>Some text 5.1.1</li>
          <li>Some text 5.1.2</li>
        </ul>
        <h3>Title 5.2</h3>
        <ul>
          <li>Some text 5.2.1</li>
          <li>Some text 5.2.2</li>
          <li>Some text 5.2.3</li>
        </ul>
      fr: |
        <h3>Titre 5.1</h3>
        <ul>
          <li>Texte quelconque 5.1.1</li>
          <li>Texte quelconque 5.1.2</li>
        </ul>
        <h3>Titre 5.2</h3>
        <ul>
          <li>Texte quelconque 5.2.1</li>
          <li>Texte quelconque 5.2.2</li>
          <li>Texte quelconque 5.2.3</li>
        </ul>
    title:
      en: Big title 5
      fr: Gros titre 5
  screenshot: # link to image
    alt:
      en: Component specification
      fr:
    link: /assets/img/radio-buttons/spec.png
layout-options:
  - option:
      en:
      fr:
name:
  en: Components name
  fr: Nom de la composante
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
      en: Design pattern &num;1
      fr:
    link:
      en: ../design-patterns/pattern
      fr:
  - title:
      en: Design pattern &num;2
      fr:
    link:
      en: ../design-patterns/pattern
      fr:
release-notes:
  - notes:
      en: Some notes that could be useful
      fr:
    progress:
      en: Beta # alpha, beta, stable
      fr: Béta
    updated: 2020-02-01 # ISO date format YYYY-MM-DD
    version: 0.0.2 # see guidelines for semantic versioning
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
  texttag: # can markdown be uesd in yaml notation? Nope, even with the `|`
    en: Only use Component for the primary action
    fr: Seulement pour une action primaire
  uses:
    - dont:
        img:
          en: https://via.placeholder.com/390X75?text=test-eng1
          fr: https://via.placeholder.com/390X75?text=test-fra1
        alt:
          en: alt-test eng1
          fr: alt-test fra1
        en: Place a <code>component</code> here and there, and don't worry.
        fr: Placez un <code>composant</code> ici et là, et ne vous inquiétez de rien.
    - dont:
        img:
          en: https://via.placeholder.com/390X75?text=test-eng2
          fr: https://via.placeholder.com/390X75?text=test-fra2
        alt:
          en: alt-test eng2
          fr: alt-test fra2
        en: Place a <code>component</code> here and there, and do worry.
        fr: Placez un <code>composant</code> ici et là, et inquiétez vous.
    - do:
        img:
          en: https://via.placeholder.com/390X75?text=test-eng3
          fr: https://via.placeholder.com/390X75?text=test-fra3
        alt:
          en: alt-test eng3
          fr: alt-test fra3
        en: Place another <code>component</code> here and there, and don't worry
        fr: Placez un autre <code>composant</code> ici et là, et ne vous inquiétez de rien.
    - do:
        img:
          en: https://via.placeholder.com/390X75?text=test-eng4
          fr: https://via.placeholder.com/390X75?text=test-fra4
        alt:
          en: alt-test eng4
          fr: alt-test fra4
        en: Place another <code>component</code> here and there, and don't worry
        fr: Placez un <code>composant</code> ici et là, et ne vous inquiétez de rien.
---

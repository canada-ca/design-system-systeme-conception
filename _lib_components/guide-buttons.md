---
# page settings
breadcrumbs:
  - title: "Home"
    link: "/en"
  - title: "Library"
    link: "/en/library"
layout: guide-component
stylesheets:
  - href: "/assets/css/styles.css"

# technical sheet
availibility:
  - title: Photoshop
    link: "#"
  - title: Axure XP
    link:
contentTitle: Buttons
description: Call to action to let a user complete an action, find a next step or submit a form.
pagetag: Call to action to let a user complete an action, find a next step or submit a form.
permalink: en/library/components/guide-buttons
related:
  - title: Interactive questions
    link: design-patterns/interactive-questions
  - title: Form
    link: "#"
  - title: Toggle
    link: "#"
stage: Stable
updated: 2019-12-24
usage:
version: 0.1
---
<!-- Content -->
  <div class="row">
      <div class="col-md-6">
          <div class="pattern-demo mrgn-bttm-lg">
              <div class="mrgn-lft-md">
                  <h3>Base (secondary actions)</h3>
                  <button class="btn btn-default">Default</button>
                  <button class="btn btn-default active">Active</button>
                  <button class="btn btn-default disabled">Disabled</button>
                  <h3>Call to action</h3>
                  <button class="btn btn-call-to-action">Default</button>
                  <button class="btn btn-call-to-action active">Active</button>
                  <button class="btn btn-call-to-action disabled">Disabled</button>
                  <h3>Accent</h3>
                  <button class="btn btn-primary">Default</button>
                  <button class="btn btn-primary active">Active</button>
                  <button class="btn btn-primary disabled">Disabled</button>
                  <h3>Text button</h3>
                  <button class="btn btn-link">Default</button>
                  <button class="btn btn-link active">Active</button>
                  <button class="btn btn-link disabled">Disabled</button>
              </div>
          </div>
      </div>
      <div class="col-md-6">
          <ul class="list-unstyled">
              <li>
                  <details>
                      <summary>1. Base (secondary actions)</summary>
                      <h3>Sizing</h3>
                      <ul>
                          <li>Min height: 36px</li>
                          <li>Min width: 36px</li>
                      </ul>
                      <h3>Borders</h3>
                      <ul>
                          <li>Border radius: 4px</li>
                          <li>Border style: outset</li>
                          <li>Border width: 1px</li>
                          <li>Border colour: #DCDEE1</li>
                      </ul>
                      <h3>Fill</h3>
                      <ul>
                          <li>Background colour: #EAEBED</li>
                      </ul>
                      <h3>Padding</h3>
                      <ul>
                          <li>Vertical padding: 10px</li>
                          <li>Horizontal padding: 14px</li>
                      </ul>
                      <h3>Text alignment</h3>
                      <ul>
                          <li>Line height: 1.4375</li>
                          <li>Horizontal alignment: center</li>
                          <li>Vertical alignment: middle</li>
                      </ul>
                      <h3>Font</h3>
                      <ul>
                          <li>Font family: Lato, sans-serif</li>
                          <li>Font size: 16px</li>
                          <li>Text colour: #335075</li>
                      </ul>
                      <h3>Hover / Active</h3>
                      <p>Default state, except:</p>
                      <ul>
                          <li>Background colour: RGB(207, 209, 213)</li>
                          <li>Border colour: RGB(187, 191, 197)</li>
                      </ul>
                      <h3>Focus</h3>
                      <p>Default state, except:</p>
                      <ul>
                          <li>Background colour: RGB(207, 209, 213)</li>
                          <li>Border colour: RGB(152, 157, 166)</li>
                      </ul>
                  </details>
              </li>
              <li>
                  <details>
                      <summary>2. Call to action</summary>
                  </details>
              </li>
              <li>
                  <details>
                      <summary>3. Accent</summary>
                  </details>
              </li>
              <li>
                  <details>
                      <summary>4. Text button</summary>
                  </details>
              </li>
          </ul>
      </div>
  </div>
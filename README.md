# Canada.ca design system

This bilingual Jekyll site is the starting point for a single source of truth for three Canada.ca design system repositories. English pages live in `en/`. French pages live in `fr/`.

## Branch policy

Open pull requests against `main`. Use `content/` for content changes, `hotfix/` for urgent fixes, and `feat/` for features. Dependabot uses `dependabot/`.

## Workflows

- Preview build checks both language builds and uploads static artifacts.
- Preview publish uses the trusted default branch. It publishes artifacts for eligible pull requests from this repository and updates the pull request description.
- Preview cleanup removes preview and promotion files when a pull request closes. A scheduled sweep removes files the close event missed.
- Promote publishes the approved artifact for one language. Configure required reviewers for the `production-en` and `production-fr` environments.
- Dependabot deploy builds merged Dependabot changes and publishes both languages.

## GitHub settings

Set these repository variables to `owner/repository` values.

| Variable | Repository |
| --- | --- |
| `PREVIEW_HOST_REPO` | Preview host. Serve its `main` branch from the root of a GitHub Pages site. |
| `PUBLISH_REPO_EN` | English production target. |
| `PUBLISH_REPO_FR` | French production target. |

Set the `PUBLISH_APP_ID` secret to the GitHub App client ID. Set `PUBLISH_APP_PRIVATE_KEY` to the private key. Install the app on all three targets with Contents write access. GitHub supplies `GITHUB_TOKEN` to the workflows.

## Local build

1. Install and select Ruby `4.0.4`.
2. Run `bundle install`.
3. Run `bundle exec rake build` to build `_site/en/` and `_site/fr/`.

To build a local preview for pull request 42, run `JEKYLL_ENV=staging PR_NUMBER=42 bundle exec rake staging`. The output goes to `_staging/design-system/en/` and `_staging/systeme-conception/fr/`.

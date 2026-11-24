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

Set these three GitHub repository variables.

| Variable | Format | Example |
| --- | --- | --- |
| `PREVIEW_HOST_REPO` | `owner/repo:EN_DIR,FR_DIR` | `gc-proto/gc-proto.github.io:design,conception` |
| `PUBLISH_REPO_EN` | `owner/repo[:subpath]` | `gc-proto/design-live` |
| `PUBLISH_REPO_FR` | `owner/repo[:subpath]` | `gc-proto/conception-live` |

The preview host serves its `main` branch from the root of a GitHub Pages site. Set both language directories to distinct paths.

Each production variable selects a repository and can include a subpath inside that repository. Omit the colon and subpath to publish at the repository root. Root deployments keep `.git`, `CNAME`, and `.nojekyll` intact.

Use letters, digits, periods, underscores, and hyphens in each path segment. Use slashes between segments. Empty segments, single-period segments, and consecutive periods are invalid.

For pull request `N`, the preview host uses these paths.

| Content | English | French |
| --- | --- | --- |
| Staging preview | `EN_DIR/pr-preview/pr-N/` | `FR_DIR/pr-preview/pr-N/` |
| Production-config artifact | `EN_DIR/prod-artifact/pr-N/SHA/` | `FR_DIR/prod-artifact/pr-N/SHA/` |

`SHA` is the seven-character prefix of the pull request head commit. The staging base URL is the preview path with a leading slash and no trailing slash. The default Jekyll base URL is empty.

Set the `PUBLISH_APP_ID` secret to the GitHub App client ID. Set `PUBLISH_APP_PRIVATE_KEY` to the private key. Install the app on all three targets with Contents write access. GitHub supplies `GITHUB_TOKEN` to the workflows.

## Local build

1. Install and select Ruby `4.0.4`.
2. Run `bundle install`.
3. Run `bundle exec rake build` to build `_site/en/` and `_site/fr/`.

For a local preview of pull request 42, run this command with your preview target.

```sh
PREVIEW_HOST_REPO=owner/repo:alpha,beta JEKYLL_ENV=staging PR_NUMBER=42 bundle exec rake staging
```

The build writes English to `_staging/en/` and French to `_staging/fr/`.

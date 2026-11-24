#!/usr/bin/env bash
set -euo pipefail

helper="$(dirname -- "${BASH_SOURCE[0]}")/parse_target.sh"
if [[ ! -f "$helper" ]]; then
  echo "The target parser is missing." >&2
  exit 1
fi
source "$helper"

parse_publish_target 'Org/site.repo'
[[ "$TARGET_REPO" == 'Org/site.repo' && "$TARGET_SUBPATH" == '' ]]
parse_publish_target 'o/r:release_v2/en-CA/v1.2'
[[ "$TARGET_REPO" == 'o/r' && "$TARGET_SUBPATH" == 'release_v2/en-CA/v1.2' ]]

parse_preview_target 'o/o.github.io:alpha/en,beta.fr'
[[ "$TARGET_REPO" == 'o/o.github.io' && "$EN_DIR" == 'alpha/en' && "$FR_DIR" == 'beta.fr' ]]

expect_invalid() {
  local output
  if output="$("$1" "$2" 2>&1)" || [[ "$output" != ::error::* ]]; then
    printf 'Expected %s to reject %q with an error.\n' "$1" "$2" >&2
    exit 1
  fi
}

for value in '' 'o' '/r' '-o/r' 'o/..' 'o/r/extra' 'o/r:' 'o/r:/en' 'o/r:en/' \
  'o/r:en//docs' 'o/r:en/../docs' 'o/r:en/./docs' 'o/r:a..b' 'o/r:en,fr' \
  'o/r:en:fr' 'o/r:en fr' $'o/r:en\n'; do
  expect_invalid parse_publish_target "$value"
done

for value in '' 'o/r' 'o/r:en' 'o/r:,fr' 'o/r:en,' 'o/r:en,en' 'o/r:en,fr,extra' \
  'o/r:/en,fr' 'o/r:en,fr/' 'o/r:en,fr//docs' 'o/r:en/../docs,fr' 'o/r:en,fr/.' \
  'o/r:en,fr?' $'o/r:en,fr\n'; do
  expect_invalid parse_preview_target "$value"
done

echo "Target parser tests passed."

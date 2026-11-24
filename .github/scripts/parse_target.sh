#!/usr/bin/env bash
# Source this file. Each parser sets TARGET_REPO and the applicable paths.

valid_target_path() {
  local LC_ALL=C
  local pattern='^[A-Za-z0-9._-]+(/[A-Za-z0-9._-]+)*$'
  [[ "$1" =~ $pattern && "$1" != *..* && "/$1/" != */./* ]]
}

parse_publish_target() {
  local LC_ALL=C
  local pattern='^([A-Za-z0-9][A-Za-z0-9-]*/[A-Za-z0-9._-]+)(:([A-Za-z0-9._/-]+))?$'
  local value="${1-}" repo subpath
  if [[ "$value" =~ $pattern ]]; then
    repo="${BASH_REMATCH[1]}"
    subpath="${BASH_REMATCH[3]}"
    if [[ "${repo#*/}" != . && "${repo#*/}" != .. ]] &&
      { [[ -z "$subpath" ]] || valid_target_path "$subpath"; }; then
      TARGET_REPO="$repo"
      TARGET_SUBPATH="$subpath"
      return 0
    fi
  fi
  echo "::error::Publish target must use owner/repo or owner/repo:subpath with a valid path." >&2
  return 1
}

parse_preview_target() {
  local LC_ALL=C
  local pattern='^([^:]+):([A-Za-z0-9._/-]+),([A-Za-z0-9._/-]+)$'
  local value="${1-}" repo en fr
  if [[ "$value" =~ $pattern ]]; then
    repo="${BASH_REMATCH[1]}"
    en="${BASH_REMATCH[2]}"
    fr="${BASH_REMATCH[3]}"
    if parse_publish_target "$repo" 2>/dev/null && valid_target_path "$en" &&
      valid_target_path "$fr" && [[ "$en" != "$fr" ]]; then
      EN_DIR="$en"
      FR_DIR="$fr"
      return 0
    fi
  fi
  echo "::error::PREVIEW_HOST_REPO must use owner/repo:EN_DIR,FR_DIR with two distinct valid paths." >&2
  return 1
}

# Call before using a parsed path in a checkout. Missing directories are valid.
check_checkout_path() {
  local path="$1" relative="$2" segment
  local -a segments
  IFS=/ read -r -a segments <<< "$relative"
  for segment in "${segments[@]}"; do
    path="$path/$segment"
    if [[ "$segment" == .[gG][iI][tT] || -L "$path" || ( -e "$path" && ! -d "$path" ) ]]; then
      printf '::error::Unsafe checkout directory: %s\n' "$path" >&2
      return 1
    fi
  done
}

# Replace the selected site and keep existing root-only exclusions.
replace_site() {
  local source_dir="$1" checkout="$2" subpath="$3" destination unexpected protected_status
  local -a exclusions=(--exclude=/.git)
  if [[ ! -d "$source_dir" ]]; then
    printf '::error::Site output directory is missing: %s\n' "$source_dir" >&2
    return 1
  fi
  unexpected="$(find "$source_dir" \( -iname .git -o ! \( -type f -o -type d \) \) -print -quit)" || return 1
  if [[ -n "$unexpected" ]]; then
    echo "::error::Site output must contain only regular files and directories outside Git metadata." >&2
    return 1
  fi

  destination="$checkout"
  if [[ -n "$subpath" ]]; then
    check_checkout_path "$checkout" "$subpath" || return 1
    destination="$checkout/$subpath"
    mkdir -p -- "$destination" || return 1
  else
    exclusions+=(--exclude=/CNAME --exclude=/.nojekyll
      --exclude=/_config.yml --exclude=/.github/ --exclude='/google*.html' --exclude=/netlify.toml)
  fi
  rsync -a --delete "${exclusions[@]}" -- "$source_dir/" "$destination/" || return 1
  if [[ -z "$subpath" ]]; then
    protected_status="$(git -C "$checkout" status --short -- CNAME .nojekyll _config.yml .github ':(glob)google*.html')" || return 1
    if [[ -n "$protected_status" ]]; then
      echo "::error::Deployment changed protected production paths." >&2
      printf '%s\n' "$protected_status" >&2
      return 1
    fi
  fi
}

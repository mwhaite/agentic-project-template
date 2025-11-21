#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd -- "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
REQUIRED_PATHS=(
  "README.md"
  "docs"
  ".github/ISSUE_TEMPLATE"
  "package.json"
)

MISSING=()
FILES_TO_SCAN=()

for path in "${REQUIRED_PATHS[@]}"; do
  FULL_PATH="${ROOT_DIR}/${path}"
  if [[ -d "${FULL_PATH}" ]]; then
    while IFS= read -r file; do
      FILES_TO_SCAN+=("${file}")
    done < <(find "${FULL_PATH}" -type f \( -name "*.md" -o -name "*.MD" -o -name "*.json" -o -name "*.yml" -o -name "*.yaml" \) | sort)
  elif [[ -f "${FULL_PATH}" ]]; then
    FILES_TO_SCAN+=("${FULL_PATH}")
  else
    MISSING+=("${path}")
  fi
done

if [[ ${#MISSING[@]} -gt 0 ]]; then
  printf 'Missing required docs/templates: %s\n' "${MISSING[*]}" >&2
  exit 1
fi

FOUND=()
for file in "${FILES_TO_SCAN[@]}"; do
  if rg --fixed-strings --quiet "TODO:" "${file}"; then
    FOUND+=("${file#${ROOT_DIR}/}")
  fi
done

if [[ ${#FOUND[@]} -gt 0 ]]; then
  printf 'TODO markers must be resolved in required docs/templates:%s\n' ""
  printf ' - %s\n' "${FOUND[@]}" >&2
  exit 1
fi

echo "Required docs/templates are free of TODO markers."

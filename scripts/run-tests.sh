#!/usr/bin/env bash
set -euo pipefail

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV_DIR="$PROJECT_DIR/.venv"

cd "$PROJECT_DIR"

if [[ ! -x "$VENV_DIR/bin/pytest" ]]; then
  echo "venv не настроен. Сначала запустите: ./scripts/setup.sh"
  exit 1
fi

MARKER="${1:-}"
if [[ -n "$MARKER" ]]; then
  "$VENV_DIR/bin/pytest" -m "$MARKER"
else
  "$VENV_DIR/bin/pytest"
fi

#!/usr/bin/env bash
set -euo pipefail

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV_DIR="$PROJECT_DIR/.venv"
PYTHON="/usr/bin/python3.12"

run_system_python() {
  env -i \
    PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin" \
    HOME="${HOME:?}" \
    USER="${USER:-$(id -un)}" \
    LANG="${LANG:-en_US.UTF-8}" \
    "$PYTHON" "$@"
}

echo "==> Проверка системного Python"
run_system_python -c "import sys; print(f'Python: {sys.executable}')"

if [[ ! -f "$PYTHON" ]]; then
  echo "Ошибка: $PYTHON не найден. Установите: sudo apt install python3.12 python3.12-venv python3-pip"
  exit 1
fi

echo "==> Удаление старого venv (если есть)"
rm -rf "$VENV_DIR"

echo "==> Создание venv"
run_system_python -m venv "$VENV_DIR"

echo "==> Установка зависимостей"
"$VENV_DIR/bin/pip" install --upgrade pip
"$VENV_DIR/bin/pip" install -r "$PROJECT_DIR/requirements.txt"

if [[ ! -f "$PROJECT_DIR/.env" ]]; then
  cp "$PROJECT_DIR/.env.example" "$PROJECT_DIR/.env"
  echo "==> Создан .env из .env.example"
fi

echo ""
echo "Готово! Активируйте окружение:"
echo "  source .venv/bin/activate"
echo ""
echo "Запуск тестов:"
echo "  ./scripts/run-tests.sh api"
echo "  ./scripts/run-tests.sh ui"
echo "  ./scripts/run-tests.sh smoke"

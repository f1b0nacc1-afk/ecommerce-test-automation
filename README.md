# E-commerce Test Automation Framework

![CI](https://github.com/f1b0nacc1-afk/ecommerce-test-automation/actions/workflows/ci.yml/badge.svg)
![Docker](https://github.com/f1b0nacc1-afk/ecommerce-test-automation/actions/workflows/docker.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![PyTest](https://img.shields.io/badge/PyTest-8.3-green)
![Selenium](https://img.shields.io/badge/Selenium-4.27-43B02A?logo=selenium)
![License](https://img.shields.io/badge/License-MIT-yellow)

Фреймворк автоматизации тестирования **UI** и **API** на Python с паттерном **Page Object Model**.

| UI | API |
|----|-----|
| [SauceDemo](https://www.saucedemo.com) | [JSONPlaceholder](https://jsonplaceholder.typicode.com) |

## Стек

Python 3.12 · PyTest · Selenium 4 · Requests · Allure · Docker · GitHub Actions

## Структура проекта

```
├── config/           # Настройки
├── pages/            # Page Object Model
├── tests/
│   ├── ui/           # UI-тесты
│   └── api/          # API-тесты
├── utils/            # API-клиент
├── data/             # Тестовые данные
├── scripts/          # setup.sh, run-tests.sh
├── docs/             # Документация
├── conftest.py
├── Dockerfile
└── docker-compose.yml
```

## Покрытие

| Тип | Тестов | Сценарии |
|-----|--------|----------|
| UI | 12 | Авторизация, корзина, checkout, сортировка |
| API | 7 | Users и Posts — GET, POST, PUT, DELETE |

## Быстрый старт

```bash
chmod +x scripts/*.sh
./scripts/setup.sh
source .venv/bin/activate

./scripts/run-tests.sh api     # API (~5 сек)
./scripts/run-tests.sh ui      # UI
./scripts/run-tests.sh smoke   # Smoke
pytest                         # Все тесты
```

## Docker

```bash
docker compose build
docker compose run --rm api-tests
docker compose run --rm ui-tests
docker compose run --rm smoke-tests
```

## Переменные окружения

Скопируйте `.env.example` → `.env`

| Переменная | По умолчанию |
|------------|--------------|
| `BASE_URL` | `https://www.saucedemo.com` |
| `HEADLESS` | `true` |
| `STANDARD_USER` | `standard_user` |
| `STANDARD_PASSWORD` | `secret_sauce` |

## Документация

- [Публикация и оформление репозитория](docs/publishing.md)

## Лицензия

[MIT](LICENSE)

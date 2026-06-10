# v1.0.0

Первый релиз фреймворка автоматизации тестирования.

## Возможности

- UI-тесты на Selenium 4 с Page Object Model (SauceDemo)
- API-тесты на Requests (JSONPlaceholder)
- PyTest fixtures, маркеры smoke/ui/api
- Docker и docker-compose
- GitHub Actions: CI + Docker pipeline
- Allure-ready структура

## Покрытие

- 12 UI-тестов: авторизация, корзина, checkout
- 7 API-тестов: users, posts

## Запуск

```bash
./scripts/setup.sh
./scripts/run-tests.sh smoke
docker compose run --rm smoke-tests
```

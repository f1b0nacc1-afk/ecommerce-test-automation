# E-commerce Test Automation Framework

![CI](https://github.com/f1b0nacc1-afk/ecommerce-test-automation/actions/workflows/ci.yml/badge.svg)
![Docker](https://github.com/f1b0nacc1-afk/ecommerce-test-automation/actions/workflows/docker.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![PyTest](https://img.shields.io/badge/PyTest-8.3-green)
![Selenium](https://img.shields.io/badge/Selenium-4.27-43B02A?logo=selenium)
![License](https://img.shields.io/badge/License-MIT-yellow)

Secondary portfolio project: a **Python** UI + API test automation framework using **Page Object Model (POM)**, PyTest, Selenium, Requests, Allure, Docker, and GitHub Actions.

| Layer | Demo target | Role |
|-------|-------------|------|
| UI | [SauceDemo](https://www.saucedemo.com) | Browser e2e flows (login, cart, checkout) |
| API | [JSONPlaceholder](https://jsonplaceholder.typicode.com) | HTTP CRUD checks against a public fake REST API |

This is a **learning / interview demo** against public targets — not a production ecommerce product and not an AI/CV project.

## Stack

Python 3.12 · PyTest · Selenium 4 · Requests · Allure · Docker · GitHub Actions

## Architecture (POM)

**UI** — page classes under `pages/` encapsulate locators and actions. Tests under `tests/ui/` call page methods via fixtures (`login_page`, `inventory_page`, `cart_page`, `logged_in_user`); they do not embed raw selectors.

**API** — `utils/APIClient` wraps a `requests.Session` (GET/POST/PUT/DELETE). Tests under `tests/api/` assert status codes and JSON fields against JSONPlaceholder.

```
├── config/           # Settings from env (.env)
├── pages/            # Page Object Model (UI)
├── tests/
│   ├── ui/           # Selenium scenarios
│   └── api/          # HTTP scenarios
├── utils/            # API client
├── data/             # Shared test data
├── scripts/          # setup.sh, run-tests.sh (Linux/macOS)
├── docs/             # Publishing notes, interview talking points
├── conftest.py       # Driver, page, API fixtures; failure screenshots
├── Dockerfile
└── docker-compose.yml
```

## Coverage (from collected tests)

Counts below match PyTest collection with parametrization (not marketing estimates).

| Layer | Collected tests | Covered scenarios |
|-------|-----------------|-------------------|
| UI | 12 | Login (valid users, invalid cases, locked-out), cart add/multi/verify, checkout, price sort |
| API | 7 | Users: list, get by id, create · Posts: by user, by id, update, delete |

### Not covered (intentionally out of scope for this demo)

- Contract / JSON Schema validation in tests (`jsonschema` is a dependency but unused)
- Parallel execution via `pytest-xdist` (available, not wired into scripts/CI)
- Cart remove, logout, checkout field validation, mobile viewports
- Auth, rate limits, or negative HTTP status matrices beyond what the demo APIs expose
- Visual / accessibility / performance testing

## Run locally

Requires **Python 3.12+**, Chrome (for UI), and network access to SauceDemo / JSONPlaceholder.

### Cross-platform (pip + pytest)

```bash
python -m venv .venv

# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate

pip install -r requirements.txt
cp .env.example .env   # Windows: copy .env.example .env

pytest -m api                              # API only
pytest -m ui                               # UI (headless via HEADLESS=true)
pytest -m smoke                            # Smoke markers
pytest                                     # Full suite
pytest --alluredir=allure-results          # Collect Allure results
```

### Linux/macOS helper scripts

```bash
chmod +x scripts/*.sh
./scripts/setup.sh
source .venv/bin/activate

./scripts/run-tests.sh api
./scripts/run-tests.sh ui
./scripts/run-tests.sh smoke
```

`scripts/setup.sh` expects system Python at `/usr/bin/python3.12`. On Windows, use the pip flow above.

## Docker

```bash
docker compose build
docker compose run --rm api-tests
docker compose run --rm ui-tests
docker compose run --rm smoke-tests
docker compose run --rm all-tests
```

UI containers use Chromium + chromedriver bundled in the image (`CHROME_BIN` / `CHROMEDRIVER_PATH`).

## Allure

Tests use `@allure.feature` / `@allure.story` / `@allure.title`. CI uploads `allure-results` artifacts.

Locally (with [Allure CLI](https://docs.qameta.io/allure/) installed):

```bash
pytest --alluredir=allure-results
allure serve allure-results
```

On UI failure, `conftest.py` also saves a screenshot under `screenshots/`.

## Environment

Copy `.env.example` → `.env`. SauceDemo values are **public demo accounts** from the SauceDemo site — not production secrets.

| Variable | Default |
|----------|---------|
| `BASE_URL` | `https://www.saucedemo.com` |
| `HEADLESS` | `true` |
| `STANDARD_USER` | `standard_user` |
| `STANDARD_PASSWORD` | `secret_sauce` |
| `JSONPLACEHOLDER_BASE_URL` | `https://jsonplaceholder.typicode.com` |

Do not commit real credentials. Keep secrets out of the repo.

## CI

GitHub Actions:

- [ci.yml](.github/workflows/ci.yml) — API and UI jobs, Allure results upload
- [docker.yml](.github/workflows/docker.yml) — image build + API / smoke in Compose

## Documentation

- [Interview talking points](docs/INTERVIEW.md) — POM, flakiness, test pyramid, skill transfer
- [Publishing checklist](docs/publishing.md)
- [Release notes](docs/release-notes.md)

## Limitations

- Depends on **third-party public demos**; availability and UI/API drift can break runs without code changes.
- JSONPlaceholder create/update/delete are **fake** (no durable persistence).
- UI suite is Chrome-only; no cross-browser matrix.
- Helper scripts are Linux-oriented; Windows users should use `venv` + `pytest` directly.
- Secondary portfolio piece for QA automation interviews — not positioned as a production framework or an AI/CV showcase.

## What I would do next

- Add JSON Schema (or OpenAPI-driven) checks for API responses
- Wire `pytest-xdist` for API and carefully for UI where isolation allows
- Explicit waits / retry policies for known flaky UI steps; reduce reliance on implicit wait alone
- Expand UI negatives (remove from cart, checkout validation) and a thin contract suite for API errors
- Publish Allure HTML from CI (e.g. Pages or a report job) instead of raw artifacts only
- Optional Playwright or second browser to compare wait strategies

## License

[MIT](LICENSE)

# Interview talking points

Short answers for international QA / SDET interviews. This repo is a **secondary portfolio project** (Python UI + API automation on public demos). It is not an AI or computer-vision product.

## Why Page Object Model (POM)?

- **Separation of concerns:** locators and UI actions live in page classes (`pages/`); tests describe intent and assertions.
- **Maintainability:** when SauceDemo changes a selector, you update one page method instead of every test.
- **Readability:** `login_page.login(...)` / `inventory_page.add_product_to_cart_by_index(0)` reads like a business step.
- **Reuse:** fixtures (`logged_in_user`) compose pages without duplicating login boilerplate.
- **Trade-off:** over-abstracting too early (deep inheritance, “god” pages) can hurt clarity — keep pages thin and flow-oriented.

## Strategies against flaky UI tests

What this project already leans on:

- Explicit waits in `BasePage` (`WebDriverWait` + expected conditions) for find/click/visibility
- Headless Chrome with stable window size in CI/Docker
- Failure screenshots via `pytest_runtest_makereport`
- Isolating UI vs API markers so API noise does not block browser jobs

What to discuss as next steps (not all implemented here):

- Prefer **explicit** waits over long implicit waits; avoid fixed `sleep`
- Idempotent setup/teardown; one browser per test (function-scoped driver)
- Quarantine / retry only for known infrastructure flakes, not to hide product bugs
- Stabilize on test IDs (`data-test`) when the app provides them (SauceDemo does)
- Run UI less often than API (pyramid); keep smoke thin

## API vs UI and the test pyramid

| Layer | Cost / speed | Feedback | Role in this repo |
|-------|--------------|----------|-------------------|
| API | Fast, cheap | Contract & logic | JSONPlaceholder CRUD smoke |
| UI e2e | Slow, brittle | User-visible paths | SauceDemo critical flows |

Pyramid idea: many fast API (or unit/integration) checks, fewer UI journeys for paths that only the browser can prove. This demo is intentionally **small** on both sides — enough to show structure, not a full product suite.

## How the skill transfers to CV / eval pipelines

Automation craft transfers even when the domain is different (e.g. evaluation stands for models or CV systems):

| Practice here | Transfer |
|---------------|----------|
| Clear fixtures and markers | Stable eval harnesses (smoke vs full regression) |
| Separation of client vs scenarios | Separate “runner / I/O” from “assertions / metrics collection” |
| CI artifacts (Allure, screenshots) | Logs, failed cases, sample outputs for triage |
| Dockerized runs | Reproducible eval environments |
| Honest coverage + limitations | Document what the stand measures and what it does not |

You still need domain-specific checks (labels, IoU, latency, dataset versions). The transferable part is **discipline**: isolation, repeatability, reporting, and not claiming metrics you did not measure.

## Honest positioning

- Demo targets: SauceDemo + JSONPlaceholder (public).
- Credentials in `.env.example` are SauceDemo’s **published** demo users, not real production secrets.
- Do not present this repo as a main AI project or as Yandex Crowd work.

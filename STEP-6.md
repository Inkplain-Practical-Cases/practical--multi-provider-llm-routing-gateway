# STEP-6 — Deployment readiness and regression tests

The final educational gateway combines typed request validation, fake OpenAI/Claude adapters, threshold-based routing, bounded transient fallback, safe 503 response mapping, and full regression coverage. GitHub Actions runs Python 3.11 `pytest` on each branch push and main.

Run `pip install -r requirements.txt && python -m pytest -q` and start `uvicorn app.main:app --reload`. No API key is needed because all provider adapters are deterministic fixtures. Production SDK support, quotas, cost accounting and persistent observability are intentionally out of scope.

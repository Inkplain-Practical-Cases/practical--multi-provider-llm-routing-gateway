# Multi-Provider LLM Routing Gateway

An educational, deterministic FastAPI gateway demonstrating a unified LLM API, OpenAI/Claude fixture adapters, automatic routing policy, transient fallback, controlled 503 errors, tests and CI. **The adapters are offline fixtures, not real hosted provider API integrations.**

## Learning branches

1. `step-01-unified-request-and-response-contract` — typed gateway contract
2. `step-02-provider-adapters-and-deterministic-offl` — injected fake providers
3. `step-03-policy-based-provider-selection` — deterministic prompt-size routing
4. `step-04-bounded-provider-fallback` — one-shot transient failover
5. `step-05-gateway-errors-and-request-tracing` — controlled HTTP errors
6. `step-06-deployment-readiness-and-regression-test` — CI and regression tests

Each branch contains `STEP-N.crd` and `STEP-N.md` for that stage. Checkout branches in order. The main branch is the final cumulative code with `FINAL.crd` and `multi-provider-llm-routing-gateway.inkp` (six STEP tabs).

## Run

`python -m pip install -r requirements.txt`

`python -m pytest -q`

`uvicorn app.main:app --reload`

POST `/v1/completions` with JSON `{"prompt":"hello", "preferred_provider":"auto"}`. Valid provider values: auto, openai, claude. No external keys are needed. Do not use as a production proxy without provider SDKs, auth, tenant quotas, billing and trace sanitization.

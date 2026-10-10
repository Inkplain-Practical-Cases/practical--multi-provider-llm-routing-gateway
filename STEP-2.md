# STEP-2 — Provider adapters and deterministic offline fakes

This branch is cumulative: the typed HTTP contract from STEP-1 remains unchanged, while an injected `ProviderCatalog` now owns two isolated fake adapters. `preferred_provider=auto` chooses the OpenAI fixture; `claude` chooses the Claude fixture. Neither calls a network or requires credentials.

Run `python -m pip install -r requirements.txt` and `python -m pytest -q`. Start with `uvicorn app.main:app --reload`, then POST `{"prompt":"Hello","preferred_provider":"claude"}` to `/v1/completions`. Confirm `provider=claude-fixture`, deterministic text and trace. Invalid provider names and blank prompts still return 422.

The next branch introduces a real Claude adapter boundary with credentials supplied through environment configuration, while offline tests remain default.

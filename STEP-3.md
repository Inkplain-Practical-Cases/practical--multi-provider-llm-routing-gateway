# STEP-3 — Policy-based provider selection

The request's `auto` preference now selects the OpenAI fixture for short prompts and Claude for prompts longer than 500 characters. An explicit preference overrides this policy. This deterministic heuristic is educational, not a real quality or cost classifier.

Run `pip install -r requirements.txt && python -m pytest -q`. Start with `uvicorn app.main:app` and POST `{"prompt":"hello"}` to `/v1/completions`. Compare it with a 501-character prompt. See `STEP-3.crd` for component relationships.

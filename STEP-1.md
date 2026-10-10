# STEP-1 — Unified request and response contract

The API accepts a validated `CompletionRequest` and returns a stable `CompletionResponse`. This branch deliberately uses a deterministic offline fixture instead of a real LLM. The HTTP door delegates to a handler, which delegates to a service, which invokes the injected provider.

## Run

```bash
python -m pip install -r requirements.txt
python -m pytest -q
uvicorn app.main:app --reload
```

POST `/v1/completions` with JSON `{ "prompt": "Hello", "preferred_provider": "auto" }`. Expect a response with `provider`, `text` and `trace_id`. Blank prompts, oversized prompts and unknown providers must produce HTTP 422.

## Next

STEP-2 introduces explicit provider adapters and deterministic offline fakes without changing the public contract.

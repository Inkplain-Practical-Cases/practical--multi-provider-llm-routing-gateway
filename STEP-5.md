# STEP-5 — Gateway errors and request tracing

The gateway returns HTTP 503 with a safe generic error when both providers experience connectivity failures. Successful responses retain a deterministic short trace ID as an educational correlation field; this is not a production request identifier.

Run `python -m pytest -q`, then test the `/v1/completions` endpoint with a mock failing provider. Compare the door's error-mapping responsibility in `STEP-5.crd`.

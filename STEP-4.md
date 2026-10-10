# STEP-4 — Bounded provider fallback

Transient `TimeoutError` and `ConnectionError` from the first provider switch to the alternate exactly once. The response identifies which provider completed the call. Validation and other failures are not silently retried. A second failure propagates; production deployment should map it to a controlled 503.

Run `python -m pytest -q` to verify successful failover and no unbounded retry. Inspect `STEP-4.crd` for the updated service component.

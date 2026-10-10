# Execute a selected provider once, and bound failover to a single alternate attempt.
# ICS layer: service; CRD component: be.service_complete
# Called by: completion handler; Calls: catalog.resolve and adapter.complete.
# Why it exists: transient provider faults should not propagate when a safe alternate exists.
# Without it: one upstream outage disables all completions.
# Step: changed in step 4 to add bounded fallback.
from hashlib import sha256
from app.contracts.completion_request import CompletionRequest
from app.contracts.completion_response import CompletionResponse
from app.providers.provider_catalog import ProviderCatalog

def service_complete(request: CompletionRequest, catalog: ProviderCatalog) -> CompletionResponse:
    """Execute at most two provider attempts and return the successful provider."""
    preferred, adapter = catalog.resolve(request.preferred_provider, request.prompt)
    try:
        # First attempt preserves explicit provider preference and auto routing policy.
        answer = adapter.complete(request.prompt)
        selected = preferred
    except (TimeoutError, ConnectionError):
        # Only transient connectivity faults trigger fallback; validation faults do not.
        selected = 'claude' if preferred == 'openai' else 'openai'
        _, alternate = catalog.resolve(selected, request.prompt)
        # Second failure propagates; we never loop or retry indefinitely.
        answer = alternate.complete(request.prompt)
    trace = sha256(f'{selected}:{request.prompt}'.encode('utf-8')).hexdigest()[:12]
    return CompletionResponse(provider=f'{selected}-fixture', text=answer, trace_id=trace)

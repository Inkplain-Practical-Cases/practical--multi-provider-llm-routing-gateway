# Service resolves a size-aware provider and returns one stable public response.
# ICS layer: service; CRD component: be.service_complete
# Called by: handle_completion; Calls: ProviderCatalog.resolve and provider.complete.
# Without it: transport must know model-specific choices.
# Step: changed in step 3 to pass prompt context to routing.
from hashlib import sha256
from app.contracts.completion_request import CompletionRequest
from app.contracts.completion_response import CompletionResponse
from app.providers.provider_catalog import ProviderCatalog

def service_complete(request: CompletionRequest, catalog: ProviderCatalog) -> CompletionResponse:
    """Select a fake provider, execute it, and return the unified response."""
    provider_name, adapter = catalog.resolve(request.preferred_provider, request.prompt)
    text = adapter.complete(request.prompt)
    trace_id = sha256(f'{provider_name}:{request.prompt}'.encode('utf-8')).hexdigest()[:12]
    return CompletionResponse(provider=f'{provider_name}-fixture', text=text, trace_id=trace_id)

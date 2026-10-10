# Service selects a deterministic provider and shapes the stable response.
from hashlib import sha256
from app.contracts.completion_request import CompletionRequest
from app.contracts.completion_response import CompletionResponse
from app.providers.provider_catalog import ProviderCatalog

def service_complete(request: CompletionRequest, catalog: ProviderCatalog) -> CompletionResponse:
    provider_name, adapter = catalog.resolve(request.preferred_provider)
    text = adapter.complete(request.prompt)
    trace_id = sha256(f'{provider_name}:{request.prompt}'.encode('utf-8')).hexdigest()[:12]
    return CompletionResponse(provider=f'{provider_name}-fixture', text=text, trace_id=trace_id)

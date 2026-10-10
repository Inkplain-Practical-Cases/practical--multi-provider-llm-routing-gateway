# Handler forwards validated intent and injected catalog to one service.
from app.contracts.completion_request import CompletionRequest
from app.contracts.completion_response import CompletionResponse
from app.providers.provider_catalog import ProviderCatalog
from app.feature_completion.services.service_complete import service_complete

def handle_completion(request: CompletionRequest, catalog: ProviderCatalog) -> CompletionResponse:
    return service_complete(request, catalog)

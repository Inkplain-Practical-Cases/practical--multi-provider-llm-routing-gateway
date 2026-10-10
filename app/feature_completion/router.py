# HTTP door: validate typed request and delegate to the handler.
from fastapi import APIRouter, Depends
from app.contracts.completion_request import CompletionRequest
from app.contracts.completion_response import CompletionResponse
from app.core.dependencies import get_completion_provider
from app.providers.provider_catalog import ProviderCatalog
from app.feature_completion.handlers.handle_completion import handle_completion

router = APIRouter()

@router.post('/v1/completions', response_model=CompletionResponse)
def complete(request: CompletionRequest, catalog: ProviderCatalog = Depends(get_completion_provider)) -> CompletionResponse:
    return handle_completion(request, catalog)

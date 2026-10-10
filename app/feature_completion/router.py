# Translate exhausted upstream provider errors into consistent HTTP gateway failures.
# ICS layer: door; CRD component: be.complete
# Called by: FastAPI; Calls: handle_completion
# Why it exists: avoid exposing transport exceptions and provider internals to clients.
# Without it: failed calls produce uncontrolled HTTP 500 responses.
# Step: changed in step 5 to map exhausted network errors.
from fastapi import APIRouter, Depends, HTTPException
from app.contracts.completion_request import CompletionRequest
from app.contracts.completion_response import CompletionResponse
from app.core.dependencies import get_completion_provider
from app.providers.provider_catalog import ProviderCatalog
from app.feature_completion.handlers.handle_completion import handle_completion

router = APIRouter()

@router.post('/v1/completions', response_model=CompletionResponse)
def complete(request: CompletionRequest, catalog: ProviderCatalog = Depends(get_completion_provider)) -> CompletionResponse:
    """Validate request, invoke the handler and hide upstream exception details."""
    try:
        # Preserve the normal typed contract for valid successful requests.
        return handle_completion(request, catalog)
    except (TimeoutError, ConnectionError) as exc:
        # A deliberately generic 503 prevents leaking provider responses or credentials.
        raise HTTPException(status_code=503, detail='LLM providers temporarily unavailable') from exc

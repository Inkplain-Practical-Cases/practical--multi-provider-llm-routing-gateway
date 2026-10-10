# HTTP door validates the request and delegates all work to the handler.
from fastapi import APIRouter, Depends
from app.contracts.completion_request import CompletionRequest
from app.contracts.completion_response import CompletionResponse
from app.core.dependencies import get_completion_provider
from app.providers.fake_provider import FakeProvider
from app.feature_completion.handlers.handle_completion import handle_completion

router = APIRouter()

@router.post('/v1/completions', response_model=CompletionResponse)
def complete(request: CompletionRequest, provider: FakeProvider = Depends(get_completion_provider)) -> CompletionResponse:
    return handle_completion(request, provider)

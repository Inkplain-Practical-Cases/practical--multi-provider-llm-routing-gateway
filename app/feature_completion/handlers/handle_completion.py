# Handler coordinates the completion use case without external I/O.
from app.contracts.completion_request import CompletionRequest
from app.contracts.completion_response import CompletionResponse
from app.providers.fake_provider import FakeProvider
from app.feature_completion.services.service_complete import service_complete

def handle_completion(request: CompletionRequest, provider: FakeProvider) -> CompletionResponse:
    return service_complete(request, provider)

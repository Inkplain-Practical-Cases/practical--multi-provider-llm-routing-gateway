# Service calls the injected provider and returns the stable response contract.
from hashlib import sha256
from app.contracts.completion_request import CompletionRequest
from app.contracts.completion_response import CompletionResponse
from app.providers.fake_provider import FakeProvider

def service_complete(request: CompletionRequest, provider: FakeProvider) -> CompletionResponse:
    text = provider.complete(request.prompt)
    trace_id = sha256(request.prompt.encode('utf-8')).hexdigest()[:12]
    return CompletionResponse(provider='offline-fixture', text=text, trace_id=trace_id)

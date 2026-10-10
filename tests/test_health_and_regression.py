# Exercise the public API after all routing and failure behavior is assembled.
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_gateway_smoke():
    """Basic final contract still returns an answer from the configured offline fake."""
    result = client.post('/v1/completions', json={'prompt': 'final integration'})
    assert result.status_code == 200
    payload = result.json()
    assert payload['provider'] == 'openai-fixture'
    assert payload['text'].startswith('OpenAI fixture:')
    assert len(payload['trace_id']) == 12

def test_regression_rejects_untrusted_provider():
    """Schema validation continues to reject unknown providers."""
    result = client.post('/v1/completions', json={'prompt': 'hello', 'preferred_provider': 'third-party'})
    assert result.status_code == 422

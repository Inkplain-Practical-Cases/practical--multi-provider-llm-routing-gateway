# Validate the new selection policy without contacting paid endpoints.
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_long_auto_prompt_routes_to_claude():
    """A long auto request chooses the alternative deterministic provider."""
    response = client.post('/v1/completions', json={'prompt': 'a' * 501})
    assert response.status_code == 200
    assert response.json()['provider'] == 'claude-fixture'

def test_explicit_provider_overrides_size():
    """Caller intent takes precedence over the automatic size threshold."""
    response = client.post('/v1/completions', json={'prompt': 'a' * 501, 'preferred_provider': 'openai'})
    assert response.json()['provider'] == 'openai-fixture'

# Verify controlled public errors when both providers fail.
from fastapi.testclient import TestClient
from app.main import app
from app.core.dependencies import get_completion_provider

class Fails:
    def complete(self, prompt):
        raise TimeoutError('secret upstream detail')

class BadCatalog:
    def resolve(self, requested, prompt=''):
        return ('claude' if requested == 'claude' else 'openai'), Fails()

def test_upstream_exhaustion_returns_safe_503():
    """Client gets a generic service-unavailable response, never a raw stack trace."""
    app.dependency_overrides[get_completion_provider] = lambda: BadCatalog()
    try:
        response = TestClient(app).post('/v1/completions', json={'prompt': 'hello'})
        assert response.status_code == 503
        assert response.json() == {'detail': 'LLM providers temporarily unavailable'}
        assert 'secret' not in response.text
    finally:
        app.dependency_overrides.clear()

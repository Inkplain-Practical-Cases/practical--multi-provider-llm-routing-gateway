# STEP-2 tests exercise both deterministic adapters and typed failures.
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_typed_completion():
    response = client.post('/v1/completions', json={'prompt': '  Explain typed output  '})
    assert response.status_code == 200
    data = response.json()
    assert data['text'] == 'OpenAI fixture: Explain typed output'
    assert data['provider'] == 'openai-fixture'
    assert len(data['trace_id']) == 12

def test_claude_adapter_is_isolated():
    response = client.post('/v1/completions', json={'prompt': 'Explain', 'preferred_provider': 'claude'})
    assert response.status_code == 200
    assert response.json()['text'] == 'Claude fixture: Explain'
    assert response.json()['provider'] == 'claude-fixture'

def test_rejects_blank_and_oversized_prompts():
    for prompt in ['   ', 'x' * 2001]:
        assert client.post('/v1/completions', json={'prompt': prompt}).status_code == 422

def test_rejects_unknown_provider():
    assert client.post('/v1/completions', json={'prompt': 'hi', 'preferred_provider': 'unknown'}).status_code == 422

def test_deterministic_trace():
    body = {'prompt': 'same input'}
    assert client.post('/v1/completions', json=body).json() == client.post('/v1/completions', json=body).json()

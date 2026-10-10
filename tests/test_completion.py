# API contract tests run entirely offline on every learning branch.
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_typed_completion():
    response = client.post('/v1/completions', json={'prompt': '  Explain typed output  '})
    assert response.status_code == 200
    data = response.json()
    assert data['text'] == 'Offline fixture: Explain typed output'
    assert data['provider'] == 'offline-fixture'
    assert len(data['trace_id']) == 12

def test_rejects_blank_and_oversized_prompts():
    for prompt in ['   ', 'x' * 2001]:
        assert client.post('/v1/completions', json={'prompt': prompt}).status_code == 422

def test_rejects_unknown_provider():
    response = client.post('/v1/completions', json={'prompt': 'hi', 'preferred_provider': 'unknown'})
    assert response.status_code == 422

def test_deterministic_trace():
    body = {'prompt': 'same input'}
    a = client.post('/v1/completions', json=body).json()
    b = client.post('/v1/completions', json=body).json()
    assert a == b

# Prove transient failover is bounded and does not hide programming bugs.
from app.contracts.completion_request import CompletionRequest
from app.feature_completion.services.service_complete import service_complete

class BrokenAdapter:
    def __init__(self, error):
        self.error = error
        self.calls = 0
    def complete(self, prompt):
        self.calls += 1
        raise self.error

class GoodAdapter:
    def __init__(self):
        self.calls = 0
    def complete(self, prompt):
        self.calls += 1
        return 'OK'

class Catalog:
    def __init__(self, primary, alternate):
        self.adapters = {'openai': primary, 'claude': alternate}
    def resolve(self, requested, prompt=''):
        selected = 'openai' if requested == 'auto' else requested
        return selected, self.adapters[selected]

def test_fallback_after_timeout():
    """The primary times out once and Claude handles the only fallback call."""
    broken, good = BrokenAdapter(TimeoutError()), GoodAdapter()
    response = service_complete(CompletionRequest(prompt='hello'), Catalog(broken, good))
    assert response.provider == 'claude-fixture'
    assert (broken.calls, good.calls) == (1, 1)

def test_second_failure_is_not_retried():
    """Two upstream failures terminate the request rather than looping."""
    first, second = BrokenAdapter(TimeoutError()), BrokenAdapter(ConnectionError())
    try:
        service_complete(CompletionRequest(prompt='hello'), Catalog(first, second))
        assert False, 'expected second provider failure'
    except ConnectionError:
        assert (first.calls, second.calls) == (1, 1)

# Inject one startup-owned provider instead of creating one per request.
from app.providers.fake_provider import FakeProvider

_fake_provider = FakeProvider()

def get_completion_provider() -> FakeProvider:
    return _fake_provider

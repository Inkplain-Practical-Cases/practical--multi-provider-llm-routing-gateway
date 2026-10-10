# Offline provider used in STEP-1 to avoid secrets and network calls.
class FakeProvider:
    def complete(self, prompt: str) -> str:
        # The deterministic fixture lets students assert an exact response.
        return f'Offline fixture: {prompt}'

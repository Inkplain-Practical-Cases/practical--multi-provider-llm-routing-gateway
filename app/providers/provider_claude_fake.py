# Deterministic stand-in for Claude, not an API client.
class ProviderClaudeFake:
    def complete(self, prompt: str) -> str:
        return f'Claude fixture: {prompt}'

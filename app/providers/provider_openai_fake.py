# Deterministic stand-in for OpenAI, not an API client.
class ProviderOpenAIFake:
    def complete(self, prompt: str) -> str:
        # Explicit provider identity makes routing tests meaningful.
        return f'OpenAI fixture: {prompt}'

# One injected catalog owns provider adapters and the default selection.
from app.providers.provider_openai_fake import ProviderOpenAIFake
from app.providers.provider_claude_fake import ProviderClaudeFake

class ProviderCatalog:
    def __init__(self) -> None:
        self._providers = {'openai': ProviderOpenAIFake(), 'claude': ProviderClaudeFake()}

    def resolve(self, requested: str):
        # STEP-2 only chooses an explicit adapter; policy routing comes later.
        selected = 'openai' if requested == 'auto' else requested
        if selected not in self._providers:
            raise ValueError('Unknown provider')
        return selected, self._providers[selected]

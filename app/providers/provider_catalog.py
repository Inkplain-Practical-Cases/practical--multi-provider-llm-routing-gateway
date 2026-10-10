# Routes completion requests through a predictable, inspectable local provider policy.
# ICS layer: provider; CRD component: be.catalog_resolve
# Called by: service_complete; Calls: offline provider adapters
# Why it exists: centralises routing decisions without entangling transport and business code.
# Without it: routing policy would diverge across endpoints.
# Step: changed in step 3, policy-based selection.
from app.providers.provider_openai_fake import ProviderOpenAIFake
from app.providers.provider_claude_fake import ProviderClaudeFake

class ProviderCatalog:
    """Select an adapter using explicit preference or a size-aware auto policy."""
    def __init__(self) -> None:
        self._providers = {'openai': ProviderOpenAIFake(), 'claude': ProviderClaudeFake()}

    def resolve(self, requested: str, prompt: str = ''):
        """Return name and adapter; short auto prompts prefer low-cost OpenAI fixture."""
        # Explicit requests must never silently select an unrelated provider.
        selected = ('claude' if len(prompt) > 500 else 'openai') if requested == 'auto' else requested
        if selected not in self._providers:
            raise ValueError('Unknown provider')
        return selected, self._providers[selected]

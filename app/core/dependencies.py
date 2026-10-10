# A startup-owned catalog is injected into each request.
from app.providers.provider_catalog import ProviderCatalog
_catalog = ProviderCatalog()

def get_completion_provider() -> ProviderCatalog:
    return _catalog

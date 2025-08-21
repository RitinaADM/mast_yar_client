from src.application.services import ClientService
from src.infrastructure.adapters.outbound.http_adapter import HttpAdapter
from src.infrastructure.adapters.inbound.ui_adapter import UiAdapter
from src.infrastructure.config.settings import settings

def create_client():
    """Создает клиент с внедрением зависимостей."""
    http_adapter = HttpAdapter(
        post_url=settings.post_url,
        get_url=settings.get_url
    )
    ui_adapter = UiAdapter(service=None)  # Создаем сначала ui_adapter
    service = ClientService(http_port=http_adapter, ui_port=ui_adapter)
    ui_adapter.service = service  # Inject service back
    return ui_adapter
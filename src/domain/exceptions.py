class ClientError(Exception):
    """Базовое исключение для клиента."""
    pass

class EmptyTextError(ClientError):
    """Исключение для пустого текста."""
    pass

class HttpRequestError(ClientError):
    """Исключение для ошибок HTTP-запросов."""
    pass
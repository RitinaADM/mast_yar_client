from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # HTTP endpoints
    post_url: str
    get_url: str

    class Config:
        env_file = ".env"  # Load from client/.env
        env_file_encoding = "utf-8"

settings = Settings()
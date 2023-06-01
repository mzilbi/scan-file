from pydantic import BaseSettings

class Settings(BaseSettings):
    config_svc_url: str = "http://config:8000"

    class Config:
        env_file = ".env"
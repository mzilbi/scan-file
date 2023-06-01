
from aiocache import cached
from core.http import requests
from config.settings import Settings

_settings = Settings()


class Service:
    @cached(ttl=60)
    async def fetch_api_config():
        return await requests.get_request(f"{_settings.config_svc_url}/api/configs/")
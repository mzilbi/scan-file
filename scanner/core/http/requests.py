import aiohttp
from aiohttp import ClientResponseError


async def get_request(request_url: str) -> any:
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(request_url) as response_result:
                response_result.raise_for_status()

                if response_result.content_type == 'application/json':
                    return await response_result.json()
                return await response_result.text()
    except ClientResponseError as error:
        print(f'error: {error}')
        raise error
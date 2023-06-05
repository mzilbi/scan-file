from .service import Service

_max_bytes__buffer = (1024 * 1024)


async def is_blacklist_in_text(text):
    blacklist = await Service.fetch_api_config()
    print(f"blacklist: {blacklist}")
    for black_word in blacklist:
        black_word_bytes = black_word.encode()
        if black_word_bytes in text:
            return True
    return False


async def is_blacklist_in_file(file):
    while True:
        content = file.read(_max_bytes__buffer)
        if not content:
            break
        print(f"file content: {content}")
        if await is_blacklist_in_text(content):
            return True
    return False

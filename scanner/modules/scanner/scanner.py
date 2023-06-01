
from .service import Service
   
async def is_blacklist_in_text(text):
        blacklist = await Service.fetch_api_config()
        print(f"blacklist: {blacklist}")
        return any(black_word in text for black_word in blacklist)
    
async def is_blacklist_in_file(file):
        content = file.read().decode("utf-8")
        print(f"file content: {content}")
        return await is_blacklist_in_text(content)
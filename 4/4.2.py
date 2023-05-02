import asyncio
import aiohttp
from aiohttp import ClientSession
import sys
sys.path.insert(0, sys.path[0]+"/../")
from util import async_timed

# asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

@async_timed()
async def fetch_status(session: ClientSession, url: str):
    async with session.get(url) as result:
        return result.status
    
@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        url = 'https://www.example.com'
        status = await fetch_status(session, url)
        print(f"status for {url} was {status}")

# asyncio.run(main())
loop = asyncio.new_event_loop()
try:
    loop.run_until_complete(main())
finally:
    loop.close()
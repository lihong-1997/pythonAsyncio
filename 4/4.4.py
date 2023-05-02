import asyncio
import aiohttp
from aiohttp import ClientSession
import sys
sys.path.insert(0, sys.path[0]+"/../")
from util import fetch_status, async_timed

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

@async_timed()
async def main():

    async with ClientSession() as session:
        urls = ['https://www.example.com' for _ in range(40)]
        requests = [fetch_status(session, url) for url in urls]
        status = await asyncio.gather(*requests)
        print(status)

asyncio.run(main())
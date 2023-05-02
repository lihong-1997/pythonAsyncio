import asyncio
import aiohttp
from aiohttp import ClientSession
import sys
sys.path.insert(0, sys.path[0]+"/../")
from util import async_timed, fetch_status


@async_timed()
async def main():
    async with ClientSession() as session:
        fetchers = [fetch_status(session, 'https://www.example.com', 1),
                    fetch_status(session, 'https://www.example.com', 8),
                    fetch_status(session, 'https://www.example.com', 10),]
        for done_task in asyncio.as_completed(fetchers, timeout=3):
            try:
                result = await done_task
                print(result, done_task)
            except asyncio.TimeoutError:
                print("got a error")

        for task in asyncio.tasks.all_tasks():
            print(type(task))

asyncio.run(main())
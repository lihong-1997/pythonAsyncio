import asyncio
import aiohttp
from aiohttp import ClientSession
import sys
sys.path.insert(0, sys.path[0]+"/../")
from util import async_timed, fetch_status

@async_timed()
async def main():
    async with ClientSession() as session:
        fetchers = [asyncio.create_task(fetch_status(session, 'https://www.example.com')),
                    asyncio.create_task(fetch_status(session, 'https://www.example.com'))]
        done, pending = await asyncio.wait(fetchers)
        print(f"done task count: {len(done)}")
        print(f"pending task count: {len(pending)}")

        for done_task in done:
            # print(await done_task)
            print(done_task.result())


asyncio.run(main())

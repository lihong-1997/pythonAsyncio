import asyncio
import logging
from aiohttp import ClientSession
import sys
sys.path.insert(0, sys.path[0]+"/../")
from util import async_timed, fetch_status

# asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

@async_timed()
async def main():
    async with ClientSession() as session:
        fetchers = [asyncio.create_task(fetch_status(session, 'https://www.example.com')),
                    asyncio.create_task(fetch_status(session, 'python://www.example.com'))]
        done, pending = await asyncio.wait(fetchers)
        print(f"done task count: {len(done)}")
        print(f"pending task count: {len(pending)}")

        for done_task in done:
            # print(await done_task)
            if done_task.exception() is None:
                print(done_task.result())
            else:
                logging.error("Request got a exception",
                              exc_info=done_task.exception())


asyncio.run(main())

import aiohttp
import asyncio
import logging
import sys
sys.path.insert(0, sys.path[0]+"/../")
from util import async_timed, fetch_status

@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        fetchers = [asyncio.create_task(fetch_status(session, 'https://www.example.com')),
                    asyncio.create_task(fetch_status(session, 'https://www.example.com', 1)),
                    asyncio.create_task(fetch_status(session, 'https://www.example.com', 10)),]
        done, pending = await asyncio.wait(fetchers, return_when=asyncio.FIRST_COMPLETED)
        print(f"done task count: {len(done)}")
        print(f"pending task count: {len(pending)}")
        for done_task in done:
            if done_task.exception() is None:
                print(done_task.result())
            else:
                logging.error("request got an exception", exc_info=done_task.exception())
        # 无异常处理
        # for pending_task in pending:
        #     print(await pending_task)
        for pending_task in pending:
            print(await pending_task)

asyncio.run(main())


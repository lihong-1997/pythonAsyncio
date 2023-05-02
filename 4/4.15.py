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
                    asyncio.create_task(fetch_status(session, 'https://www.example.com', 3)),]
        done, pending = await asyncio.wait(fetchers, timeout=2)
        print(f"done task count: {len(done)}")
        print(f"pending task count: {len(pending)}")
        for done_task in done:
            print(done_task.result())
        # 无异常处理
        # for pending_task in pending:
        #     print(await pending_task)
        for pending_task in pending:
            print(await pending_task)
            # pending_task.cancel()

asyncio.run(main())
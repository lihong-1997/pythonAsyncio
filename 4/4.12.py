import aiohttp
import asyncio
import logging
import sys
sys.path.insert(0, sys.path[0]+"/../")
from util import async_timed, fetch_status

@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        fetchers = [asyncio.create_task(fetch_status(session, 'python://bad.com')),
                    asyncio.create_task(fetch_status(session, 'httpts://www.example.com', delay=3)),
                    asyncio.create_task(fetch_status(session, 'httpts://www.example.com', delay=3)),]
        done, pending = await asyncio.wait(fetchers, return_when=asyncio.FIRST_EXCEPTION)
        print(f"done task count: {len(done)}")
        print(f"pending task count: {len(pending)}")
        for done_task in done:
            if done_task.exception() is None:
                print(done_task.result())
            else:
                logging.error("request got an exception", exc_info=done_task.exception())
        
        for pending_task in pending:
            pending_task.cancel()

asyncio.run(main())

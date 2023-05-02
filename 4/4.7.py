import asyncio
import aiohttp
from aiohttp import ClientSession
import sys
sys.path.insert(0, sys.path[0]+"/../")
from util import delay, fetch_status

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def main1():
    results = await asyncio.gather(delay(3), delay(1))
    print(results)

async def main():
    timeout = aiohttp.ClientTimeout(total=0.5)
    async with ClientSession(timeout=timeout) as session:
        urls = ['https://www.example.com', 'python://www.example.com']
        tasks = [fetch_status(session, url) for url in urls]
        # status_codes = await asyncio.gather(*tasks, return_exceptions=True)
        # print(status_codes)
        results = await asyncio.gather(*tasks, return_exceptions=True)
        exceptions = [res for res in results if isinstance(res, Exception)]
        successful_results = [res for res in results if not isinstance(res, Exception)]
        print(f"all results {results}")
        print(f"finished successfully {successful_results}")
        print(f"threw exception {exceptions}")


asyncio.run(main())
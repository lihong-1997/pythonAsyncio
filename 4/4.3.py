import asyncio
import aiohttp
from aiohttp import ClientSession
import sys
sys.path.insert(0, sys.path[0]+"/../")
from util import async_timed, fetch_status

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# @async_timed()
# async def fetch_status(session: ClientSession, url: str):
#     ten_millis = aiohttp.ClientTimeout(total=.01)
#     async with session.get(url, timeout=ten_millis) as result:
#         return result.status
    
@async_timed()
async def main():
    session_timeout = aiohttp.ClientTimeout(total=2, connect=1)
    conn = aiohttp.TCPConnector(limit=0)
    try:
        async with aiohttp.ClientSession(connector=conn, timeout=session_timeout) as session:
            url = 'https://www.example.com'
            tasks = [asyncio.create_task(fetch_status(session, url)) for _ in range(20)]
            status = [await task for task in tasks]
            # status = await fetch_status(session, url)
            print(f"status for {url} was {status}")
    except asyncio.exceptions.TimeoutError as e:
        print("error")

# asyncio.run(main())
loop = asyncio.new_event_loop()
try:
    loop.run_until_complete(main())
finally:
    loop.close()
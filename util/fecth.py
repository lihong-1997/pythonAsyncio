from util import async_timed
import asyncio
import aiohttp
from aiohttp import ClientSession

@async_timed()
async def fetch_status(session: ClientSession, url: str, delay: int = 0):
    ten_millis = aiohttp.ClientTimeout(total=0.01)
    await asyncio.sleep(delay)
    async with session.get(url) as result:
        return result.status
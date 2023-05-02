from util import async_timed
import asyncio
import aiohttp
from aiohttp import ClientSession

@async_timed()
async def fetch_status(session: ClientSession, url: str):
    ten_millis = aiohttp.ClientTimeout(total=0.01)
    async with session.get(url, timeout=ten_millis) as result:
        return result.status
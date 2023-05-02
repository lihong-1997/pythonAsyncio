import asyncio

async def delay(delay_seconds: int) -> int:
    print(f"sleeping for {delay_seconds} second(s)")
    loop = asyncio.get_running_loop()
    print(loop)
    await asyncio.sleep(delay_seconds)
    print(f"finished sleeping for {delay_seconds} second(s)")
    return delay_seconds

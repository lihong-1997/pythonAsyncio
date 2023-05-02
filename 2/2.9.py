import asyncio
import sys
sys.path.insert(0, sys.path[0]+"/../")
from util import delay

async def main():
    sleep_for_three = asyncio.create_task(delay(3))
    sleep_again = asyncio.create_task(delay(3))
    sleep_one_more = asyncio.create_task(delay(3))
    print("all task are running")

    await sleep_for_three
    await sleep_again
    await sleep_one_more

asyncio.run(main())
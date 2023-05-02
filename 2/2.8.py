import asyncio
import sys
sys.path.insert(0, sys.path[0]+"/../")
from util import delay

async def main():
    sleep_for_three = asyncio.create_task(delay(3))
    print("is running...", type(sleep_for_three))

    result = await sleep_for_three
    print(result)

asyncio.run(main())

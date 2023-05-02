import asyncio
from asyncio import TimeoutError
import sys
sys.path.insert(0, sys.path[0]+"/../")
from util import delay

async def main():
    task = asyncio.create_task(delay(2))
    try:
        result = await asyncio.wait_for(asyncio.shield(task), 3)
        print(result) # 无输出
    except TimeoutError:
        print("Task took longer than five seconds, it will finish soon")
        result = await task
        print(result)

asyncio.run(main())
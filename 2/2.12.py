import asyncio
from asyncio import TimeoutError
import sys
sys.path.insert(0, sys.path[0]+"/../")
from util import delay

async def main():
    delay_task = asyncio.create_task(delay(2))
    try:
        result = await asyncio.wait_for(delay_task, timeout=1)
        print(result) # 无输出
    except TimeoutError:
        print("got a timeout")
        print(f"was the task cancelled?{delay_task.cancelled()}")

asyncio.run(main())
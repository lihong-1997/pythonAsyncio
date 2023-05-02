import asyncio
from asyncio import CancelledError
import sys
sys.path.insert(0, sys.path[0]+"/../")
from util import delay

async def fib(n: int) -> int:
    while n :
        n = n + 1
        if n % 2000000 == 0:
            print("n")

async def main():
    long_task = asyncio.create_task(delay(10))
    # long_task = asyncio.create_task(fib(40)) # 此时事件循环轮不到执行23行的sleep,故23行阻塞
    n = 0
    while n < 1000000:
        n = n + 0.1
    seconds_elapsed = 0

    while not long_task.done():
        
        await asyncio.sleep(1)
        seconds_elapsed = seconds_elapsed + 1
        if seconds_elapsed % 2 == 0:
            print("Task not finished, checking again in a second")
            print("sec")
        if seconds_elapsed == 5:
            long_task.cancel()
    
    try:
        await long_task
    except CancelledError:
        print("our task was cancelled")

asyncio.run(main())
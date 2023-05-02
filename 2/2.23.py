import asyncio
import sys
sys.path.insert(0, sys.path[0]+"/../")
from util import async_timed

@async_timed()
async def cpu_bound_work():
    counter = 0
    for i in range(100000000):
        counter = counter + i
    return counter

async def main():
    loop = asyncio.get_event_loop()
    loop.slow_callback_duration = .250
    task_one = asyncio.create_task(cpu_bound_work())
    await task_one

asyncio.run(main(), debug=True)
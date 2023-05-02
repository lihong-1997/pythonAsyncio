import asyncio


async def delay(delay_seconds: int) -> int:
    print(f"sleeping for {delay_seconds} second(s)")
    await asyncio.sleep(delay_seconds)
    print(f"finished sleeping for {delay_seconds} second(s)")
    return delay_seconds

async def hello_every_second():
    for i in range(10):
        await asyncio.sleep(1)
        print("I am running other code while wating!")

async def main():
    first_delay = asyncio.create_task(delay(3))
    second_delay = asyncio.create_task(delay(3))
    i = 0
    while True:
        i = i + 1
    await hello_every_second()

    # await asyncio.sleep(1)
    # i = 1
    # while True:
    #     i = i + 1
    await first_delay
    await second_delay

asyncio.run(main())
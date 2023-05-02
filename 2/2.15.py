from asyncio import Future
import asyncio

def make_request():
    future = Future()
    asyncio.create_task(set_future_value(future))
    return future

async def set_future_value(future: Future):
    await asyncio.sleep(2)
    future.set_result(42)

async def main():
    future = make_request()
    print(f"is the future done? {future.done()}")
    value = await future
    print(f"is the future done? {future.done()}")
    print(value)

asyncio.run(main())
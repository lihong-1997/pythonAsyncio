import asyncio
import sys
sys.path.insert(0, sys.path[0]+"/../")
from util import delay

def call_later():
    print("I am being called in the future")

async def main():
    loop = asyncio.get_event_loop()
    loop.call_soon(call_later)
    await delay(2)

# loop = asyncio.new_event_loop()

# try:
#     re = loop.run_until_complete(main())
# finally:
#     loop.close()

asyncio.run(main(), debug=True)
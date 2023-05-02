import asyncio
import sys
sys.path.insert(0, sys.path[0]+"/../")
from util import delay


loop = asyncio.new_event_loop()

try:
    re = loop.run_until_complete(delay(2))
finally:
    loop.close()
    print(re)
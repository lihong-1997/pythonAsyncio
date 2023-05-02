import functools
import time
from typing import Callable, Any


def async_timed():
    def wrapper(func: Callable) -> Callable:
        @functools.wraps(func)
        async def wrapped(*args, **kwargs) -> Any:
            start = time.time()
            try:
                return await func(*args, **kwargs)
            finally:
                end = time.time()
                print(f"finished {func} in {(end - start):.4f} seconds")
        return wrapped
    return wrapper
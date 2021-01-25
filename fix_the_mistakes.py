import asyncio
import logging
# import os
import os
# import datetime
from datetime import datetime

logger = logging.getLogger(__name__)
SLEEP_DURATION = os.getenv("SLEEP_DURATION")


class Pipeline:
    # removed async keyword from __init__ function
    # added self call to both functions
    # removed *args parameter since it wasn't used
    def __init__(self, **kwargs):
        default_sleep_duration = kwargs["default_sleep_duration"]

    async def sleep_for(self, coro, sleep_duration, *args, **kwargs):
        # added await keyword to sleep
        await asyncio.sleep(sleep_duration)
        # removed indent
        # formatted string properly
        logger.info("Slept for %s seconds" % sleep_duration)
        start = datetime.now()
        # changed kwarg to kwargs
        await coro(*args, **kwargs)
        end = datetime.now()
        time_elapsed = (start - end).total_seconds()
        logger.info(f"Executed the coroutine for {time_elapsed} seconds")

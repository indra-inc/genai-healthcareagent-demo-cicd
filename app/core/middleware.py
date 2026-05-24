import time

from fastapi import Request

from app.core.logging_config import logger


async def request_timing_middleware(request: Request, call_next):
    start_time = time.time()

    response = await call_next(request)

    process_time = round(time.time() - start_time, 4)

    logger.info(f"{request.method} {request.url.path} completed in {process_time} sec")

    response.headers["X-Process-Time"] = str(process_time)

    return response

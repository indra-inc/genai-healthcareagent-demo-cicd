from fastapi import Request
from fastapi.responses import JSONResponse

from app.core.logging_config import logger


async def global_exception_handler(request: Request, exc: Exception):
    logger.exception(f"Unhandled exception occurred: {str(exc)}")

    return JSONResponse(
        status_code=500, content={"status": "error", "message": "Internal Server Error"}
    )

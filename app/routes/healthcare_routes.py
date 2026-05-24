from fastapi import APIRouter

from app.core.logging_config import logger
from app.models.request_models import AgentRequest
from app.services.healthcare_service import process_healthcare_query

router = APIRouter()


@router.get("/health")
async def health_check():
    return {"status": "healthy", "service": "healthcare-agent", "version": "v1"}


@router.post("/ask")
async def ask_agent(request: AgentRequest):
    logger.info(f"Received healthcare query: {request.query}")

    response = process_healthcare_query(request.query)

    return {"response": response}

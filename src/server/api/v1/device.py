from fastapi import APIRouter


router = APIRouter()


@router.get(
    "/fetch_job",
    response_model=str,
    responses={
        200: {"description": "Search Completed"},
    },
    tags=["Ingestion"],
)
async def fetch_job() -> str:
    """
    Placeholder for Microservice endpoint to handle ingestion
    """
    return "OK"

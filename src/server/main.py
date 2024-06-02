from fastapi import FastAPI
from fastapi import status

from .api.main import app as app_v1

app = FastAPI(
    title="Remote Land Management Microservice",
    description="HTTP Microservice endpoints for managing my land remotely via IoT devices",
    version="0.0.1",
    contact={
        "name": "Jeremy Dyer",
        "url": "https://github.com/jdye64",
    },
    openapi_tags=[
        {"name": "Health", "description": "Health checks"},
    ],
)


app.mount("/v1", app_v1)


@app.get(
    "/health",
    tags=["Health"],
    summary="Perform a Health Check",
    description="""
        Immediately returns 200 when service is up.
        This does not check the health of downstream
        services.
    """,
    response_description="Return HTTP Status Code 200 (OK)",
    status_code=status.HTTP_200_OK,
)
def get_health() -> str:
    # Perform a health check
    return "OK"

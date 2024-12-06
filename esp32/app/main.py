from fastapi import FastAPI
from app.routers import example

app = FastAPI(
    title="FastAPI Project",
    description="A simple FastAPI project",
    version="0.1.0"
)

# Include routers
app.include_router(example.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI project!"}

from fastapi import FastAPI

from .v1.device import router as DeviceApiRouter

app = FastAPI()

app.include_router(DeviceApiRouter)

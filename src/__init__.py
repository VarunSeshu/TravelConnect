import uuid

import sentry_sdk
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.api.middlewares.backend_middleware import BackendMiddleware

from .api.routers import router
from .config import env
from .lib.api_response import send_response
from .lib.sentry import start_sentry

# Enable/Disable Swagger Schema
# docs_url = "/docs" if env.APP_DEBUG else None
docs_url = "/docs"
redoc_url = "/redocs"

app = FastAPI(
    title="Backend API", version="2.0.0", docs_url=docs_url, redoc_url=redoc_url
)

app.debug = env.APP_DEBUG

app.add_middleware(
    CORSMiddleware,
    allow_origins=env.ALLOWED_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    max_age=6000,
)

if not app.debug:
    start_sentry()


@app.get("/api/ping")
async def index():
    return send_response({"backend-service": {"status": "up"}})


app.middleware("http")(BackendMiddleware())

# backend APIs
app.include_router(router.router, prefix="/api")

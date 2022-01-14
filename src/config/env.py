import os

from src.api.middlewares.auth import JWTSecret

# APP_ENV = os.getenv("APP_ENV")
# APP_DEBUG = os.getenv("APP_DEBUG") in ["true", "True"]
# LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG")
# DATABASE_PORT = os.getenv("DATABASE_PORT")
# DATABASE_USER = os.getenv("DATABASE_USER")
# DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
# DATABASE_HOST=os.getenv("DATABASE_HOST")
# DATABASE_NAME=os.getenv("DATABASE_NAME")
# SENTRY_DSN = os.getenv("SENTRY_DSN")
# ALLOWED_CORS_ORIGINS = os.getenv("ALLOWED_CORS_ORIGINS")
# SENTRY_DSN = os.getenv("SENTRY_DSN")
# LOGS_DIR = os.getenv("LOGS_DIR")

APP_ENV = "local"
APP_DEBUG = True
LOG_LEVEL = "DEBUG"
DATABASE_PORT = 3356
DATABASE_USER = "root"
DATABASE_PASSWORD = "root"
DATABASE_HOST = "127.0.0.1"
DATABASE_NAME = "khunti_baazar"
LOGS_DIR = "/usr/src/backend/logs"
JWT_SECRET = "test_secret"

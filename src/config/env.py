import os

APP_ENV = os.getenv("APP_ENV")
APP_DEBUG = os.getenv("APP_DEBUG") in ["true", "True"]
LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG")
DATABASE_NAME = os.getenv("DATABASE_NAME")
DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_PORT = os.getenv("DATABASE_PORT")
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
SENTRY_DSN = os.getenv("SENTRY_DSN")
ALLOWED_CORS_ORIGINS = os.getenv("ALLOWED_CORS_ORIGINS")
SENTRY_DSN = os.getenv("SENTRY_DSN")
LOGS_DIR = os.getenv("LOGS_DIR")
ES_HOST_URL = os.getenv("ES_HOST_URL")
ES_USERNAME = os.getenv("ES_USERNAME")
ES_PASSWORD = os.getenv("ES_PASSWORD")

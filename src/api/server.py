"""
FastAPI Server
"""

from fastapi import FastAPI

from src.api.routes import router

app = FastAPI(
    title="AI Supply Chain Intelligence API",
    version="1.0.0",
)

app.include_router(router)


@app.get("/")
def home():

    return {
        "message": "AI Supply Chain Intelligence API"
    }


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }

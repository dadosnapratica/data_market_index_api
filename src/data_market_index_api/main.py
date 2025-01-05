from fastapi import FastAPI
from data_market_index_api.routes import health, fetcher

app = FastAPI(
    title="Market Index API",
    description="API for fetching market index data with health monitoring.",
    version="0.1.0",
    docs_url="/swagger",
    redoc_url="/redoc",
)

# Include routes
app.include_router(health.router)
app.include_router(fetcher.router, prefix="/api/v1")

# Run using `poetry run uvicorn market_index_api.main:app --reload`

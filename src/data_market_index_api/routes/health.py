from fastapi import APIRouter

router = APIRouter()

@router.get("/health", tags=["Health"])
def health_check():
    """
    Health Check Endpoint
    - Verifies the system is operational.
    """
    return {"status": "healthy"}

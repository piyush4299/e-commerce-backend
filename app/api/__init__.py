# app/api/__init__.py

from fastapi import APIRouter
from .v1 import router as v1_router

# Create an APIRouter instance to organize endpoints
router = APIRouter()

# Include the routers from different versions (e.g., v1, v2, etc.)
router.include_router(v1_router, prefix="/v1", tags=["v1"])

# You can include other versions as well
# router.include_router(v2_router, prefix="/v2", tags=["v2"])
# ...

# Additional global API configurations and middleware can be added here
# For example, authentication middleware, logging, etc.

# Export the 'router' instance so it can be included in the main FastAPI app
__all__ = ["router"]
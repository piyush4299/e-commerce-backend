from fastapi import APIRouter
from .products import router as product_router
from .cart import router as cart_router
from .orders import router as orders_router

router = APIRouter()

router.include_router(product_router, prefix='/products', tags=["products"])
router.include_router(cart_router, prefix='/cart', tags=["cart"])
router.include_router(orders_router, prefix='/orders', tags=["orders"])

__all__ = ["router"]
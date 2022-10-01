from fastapi import APIRouter

from app.api.v1.basic.views import router as basic_router

api_router = APIRouter()

api_router.include_router(basic_router)

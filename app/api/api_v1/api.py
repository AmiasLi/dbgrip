from fastapi import APIRouter
from app.api.api_v1.routers.instance import router as instance_router

api_router = APIRouter()

api_router.include_router(instance_router, prefix="/admin", tags=["instance"])

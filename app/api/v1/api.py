from fastapi import APIRouter
from .apis.auth import router as auth_routes

router = APIRouter()

router.include_router(auth_routes)

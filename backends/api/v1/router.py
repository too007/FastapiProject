# backends/api/v1/router.py

from fastapi import APIRouter
from backends.api.v1.endpoints import stocks
from backends.api.v1.endpoints import user

api_router = APIRouter()

api_router.include_router(stocks.router)


api_router.include_router(user.router)
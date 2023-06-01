from fastapi import APIRouter

from modules import configs

api = APIRouter()

api.include_router(configs.api, prefix="/configs")


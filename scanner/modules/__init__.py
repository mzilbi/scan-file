from fastapi import APIRouter

from modules import scanner

api = APIRouter()

api.include_router(scanner.api, prefix="/scanner")

 
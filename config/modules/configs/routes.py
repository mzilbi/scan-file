from fastapi import APIRouter, status, HTTPException, Depends

from .service import Service

router = APIRouter()

_service = Service()


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[str])
async def get(
    service: Service = Depends(_service)
):
    try:
        result = service.get()

        if result:
            return result
    except Exception as e:
        print(f"Error get config: {e}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Config not found")
    

@router.patch("/", status_code=status.HTTP_200_OK, response_model=list[str])
async def update(
    payload: list[str],
    service: Service = Depends(_service)
):
    try:
        service.update(payload)
        return service.get()
    except Exception as e:
        print(f"Error update config: {e}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
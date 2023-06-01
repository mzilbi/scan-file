from fastapi import APIRouter, status, HTTPException, Depends, UploadFile
from .scanner import is_blacklist_in_file

router = APIRouter()


async def upload_file_scan(upload_file: UploadFile):
    try:
        return "detected" if await is_blacklist_in_file(upload_file.file) else "clean"
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
    
@router.post("/", status_code=status.HTTP_200_OK, response_model=str)
async def post(
    result: str = Depends(upload_file_scan)
):
    return result

    

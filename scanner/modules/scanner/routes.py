from fastapi import APIRouter, status, HTTPException, Depends, UploadFile
import time
from .scanner import is_blacklist_in_file

router = APIRouter()


async def scan_upload_file(upload_file: UploadFile):
    try:
        return await is_blacklist_in_file(upload_file.file) 
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
    
@router.post("/", status_code=status.HTTP_200_OK, response_model=str)
async def post(
    id_detected_file: str = Depends(scan_upload_file)
):
    return "detected" if id_detected_file else "clean"

    

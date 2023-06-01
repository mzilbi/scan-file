from fastapi import FastAPI

from modules import api

app = FastAPI(title="config", description="config", version="0.0.1")

# apis
app.include_router(api, prefix="/api", tags=["Scanner svc Api"])

@app.on_event("startup")
async def startup():
    print('api is starting up')
    pass


@app.on_event("shutdown")
async def shutdown():
    print('api is shutting down')
    pass

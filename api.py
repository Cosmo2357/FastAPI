from fastapi import APIRouter

router = APIRouter()


@router.get("/apibackend")
async def read_api():
    return {"message": "Hello from API!"}

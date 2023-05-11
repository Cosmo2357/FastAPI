# tasks.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/tasks")
async def read_tasks():
    return {"message": "Hello from Tasks!"}

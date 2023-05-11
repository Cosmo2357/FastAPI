from fastapi import  FastAPI, APIRouter, APIRouter, HTTPException
from api import router as api_router
from tasks import router as tasks_router
from v1.helper import testfunc as omg
from starlette.config import Config


config = Config(".env")
POSTGRES_DB = config("POSTGRES_DB", cast=str)
print(POSTGRES_DB)

#print("Hello World")
print("Hello, world!")


app = FastAPI()
# api.py

app.include_router(api_router)
app.include_router(tasks_router)

omg.sayhello()


router = APIRouter()
@router.get("/")
async def read_api():
    return {"message": "Hello from API!"}

@app.get("/test", description="This is the root endpoint", tags=["root"])
async def root():
    return {"message": "Hello World"}  # This is the response


@app.get("/test/v1/{id}")
async def get(id: int):
    if id == 1:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": id}  # This is the response


@app.post("/hello",  tags=["group1"])
async def post():
    return {"message": "Hello World"}  # This is the response


@app.delete("/test/hello")
async def list_items():
    return {"message": "Hello World"}  # This is the response


@app.put("/hello")
async def put():
    return {"message": "Hello World"}  # This is the response

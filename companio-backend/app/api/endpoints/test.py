from fastapi import APIRouter

router = APIRouter()


@router.get("/hello_world")
async def hello_world():
    """Get current user"""
    return {"message": "Hello World. Welcome to FastAPI!"}

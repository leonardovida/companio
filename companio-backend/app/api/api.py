from fastapi import APIRouter

# from app.api.endpoints import old_routes as notes
from app.api.endpoints import auth, lists, users

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(lists.router, prefix="/lists", tags=["lists"])
# api_router.include_router(test.router, prefix="/test", tags=["test"])
# api_router.include_router(notes.router, prefix="/notes", tags=["notes"])

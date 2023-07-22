from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api import deps
from app.models import List
from app.schemas.requests import ListCreateRequest
from app.schemas.responses import ListReponse

router = APIRouter()


@router.post("/register", response_model=ListReponse)
async def register_new_list(
    new_user: ListCreateRequest,
    session: AsyncSession = Depends(deps.get_session),
):
    """Create new user"""
    result = await session.execute(select(List).where(List.email == new_user.email))
    if result.scalars().first() is not None:
        print("Email already registered.")
        # raise HTTPException(status_code=400, detail="Email already registered.")
    _list = List(
        email=new_user.email,
        city=new_user.city,
        list=new_user.list,
        phone=new_user.phone,
        service=new_user.service,
    )
    session.add(_list)
    await session.commit()
    return _list

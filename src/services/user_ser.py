from typing import Annotated

from fastapi import Depends
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.api.auth import models
from src.db import get_async_session


async def get_user(
	user_id: str | int,
	db_session: Annotated[AsyncSession, Depends(get_async_session)],
) -> models.User | None:
	user = await db_session.exec(select(models.UserInDb).where(models.UserInDb.id == user_id))
	user = user.first()
	return user

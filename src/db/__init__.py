import contextlib
from typing import Any, AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession

from src.settings import settings

async_engine = create_async_engine(settings.DB_URL_ASYNC, echo=True, future=True)


async def init_db():
	async with async_engine.begin() as conn:
		await conn.run_sync(SQLModel.metadata.create_all)


# Dependency to provide an async session
@contextlib.asynccontextmanager
async def get_async_session() -> AsyncGenerator[AsyncSession, Any]:
	async with AsyncSession(async_engine) as session:
		yield session

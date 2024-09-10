from typing import Generator

from sqlalchemy.ext.asyncio import AsyncSession
from core.database import Session


async def get_db() -> Generator:
    session: AsyncSession = Session()
    
    try:
        yield session
    finally:
        await session.close()

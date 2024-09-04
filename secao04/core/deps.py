from typing import Generator
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import Session


async def get_session() -> Generator:
    session: AsyncSession = Session()  # Executando a função classe Session

    try:
        yield session  # Retornando e aguarda a sessão para ser utilizada
    finally:
        await session.close()  # Fechando a sessão

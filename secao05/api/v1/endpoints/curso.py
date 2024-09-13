from typing import List
from fastapi import APIRouter, Depends
from fastapi import status
from fastapi import HTTPException
from fastapi import Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from models.curso_model import CursoModel
from core.deps import get_session

# ByPass warning SQLModel select
from sqlmodel.sql.expression import Select, SelectOfScalar
SelectOfScalar.inherit_cache = True  # type: ignore
Select.inherit_cache = True  # type: ignore
# Fim ByPass

router = APIRouter()


# POST CURSO
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=CursoModel)
async def post_curso(curso: CursoModel, db: AsyncSession = Depends(get_session)):
    # novo_curso = CursoModel(**curso.dict()) TESTAR!!!!
    novo_curso = CursoModel(titulo=curso.titulo,
                            aulas=curso.aulas, horas=curso.horas)
    db.add(novo_curso)
    await db.commit()

    return novo_curso


# GET CURSOS
@router.get("/", response_model=List[CursoModel])
async def get_cursos(db: AsyncSession = Depends(get_session)):
    async with db() as session:
        query = select(CursoModel)
        result = await session.execute(query)

        cursos: List[CursoModel] = result.scalars().all()
        return cursos


# GET CURSO
@router.get("/{curso_id}", response_model=CursoModel, status_code=status.HTTP_200_OK)
async def get_curso(curso_id: int, db: AsyncSession = Depends(get_session)):
    async with db() as session:
        query = select(CursoModel).filter(CursoModel.id == curso_id)
        result = await session.execute(query)
        curso = result.scalars().first()  # ??

    if not curso:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")

    return curso


# PUT CURSO
@router.put("/{curso_id}", response_model=CursoModel, status_code=status.HTTP_202_ACCEPTED)
async def put_curso(curso_id: int, curso: CursoModel, db: AsyncSession = Depends(get_session)):
    async with db() as session:
        query = select(CursoModel).filter(CursoModel.id == curso_id)
        result = await session.execute(query)
        curso_up = result.scalars().first()

        if curso_up:
            curso_up.titulo = curso.titulo
            curso_up.aulas = curso.aulas
            curso_up.horas = curso.horas

            await session.commit()

            return curso_up

        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")


# DELETE CURSO
@router.delete("/{curso_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_curso(curso_id: int, db: AsyncSession = Depends(get_session)):
    async with db() as session:
        query = select(CursoModel).filter(CursoModel.id == curso_id)
        result = await session.execute(query)
        curso_del = result.scalars().first()

        if curso_del:
            await session.delete(curso_del)
            await session.commit()

            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")

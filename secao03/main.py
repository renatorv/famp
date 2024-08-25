from typing import List, Optional

from fastapi.responses import JSONResponse
from fastapi import Response

from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status


from model import Curso

app = FastAPI()

cursos = {
    1: {
        "titulo": "Programação em Python",
        "aulas": 112,
        "horas": 58
    },
    2: {
        "titulo": "Algortimos e Lógica de Programação",
        "aulas": 87,
        "horas": 67
    },
    3: {
        "titulo": "Flutter e Dart",
        "aulas": 50,
        "horas": 100
    },
}


@app.get("/cursos")
async def get_cursos():
    return cursos


@app.get('/cursos/{curso_id}')
async def get_curso(curso_id: int):
    try:
        curso = cursos[curso_id]
        return curso
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado!")


@app.post('/cursos', status_code=status.HTTP_201_CREATED)
async def post_curso(curso: Curso):
    next_id: int = len(cursos) + 1
    cursos[next_id] = curso
    del curso.id
    return curso


@app.put('/cursos/{curso_id}')
async def put_curso(curso_id: int, curso: Curso):
    if curso_id in cursos:
        cursos[curso_id] = curso
        curso.id = curso_id
        del curso.id

        return curso
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Não existe um curos o id {curso_id}")


@app.delete('/cursos/{curso_id}')
async def delete_curso(curso_id: int):
    if curso_id in cursos:
        del cursos[curso_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
        #-------------------------------------------------------------------------------------------------
        # return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)                                    * 
        # O JSONResponse tem um bug nessa versão do FastAPI                                              * 
        #-------------------------------------------------------------------------------------------------
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Não existe um curso com o id {curso_id}")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0.",
                port=8000, debug=True, reload=True)

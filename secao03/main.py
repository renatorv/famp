from model import Curso
from model import cursos
from typing import List, Optional, Any, Dict

from fastapi.responses import JSONResponse
from fastapi import Response
from fastapi import Path
from fastapi import Query
from fastapi import Header

from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from fastapi import Depends

from time import sleep


def fake_db():
    try:
        print("Abrindo conexão com o banco de dados...")
        sleep(1)
    finally:
        print("Fechando conexão com o banco de dados...")
        sleep(1)


app = FastAPI(title='API de Cursos', version='1.2',
              description='Uma API de estudo do FastAPI',)


@app.get("/cursos", description="Retorna todos os cursos ou uma lista vazia", summary="Retorna todos os cursos",
         response_model=List[Curso], response_description="Cursos retornados com sucesso")
async def get_cursos(db: Any = Depends(fake_db)):
    return cursos


@app.get('/cursos/{curso_id}')
async def get_curso(curso_id: int = Path(default=None, title="O ID do curso", description="Deve ser entre 1 e 3", gt=0, lt=4), db: Any = Depends(fake_db)):
    try:
        curso = cursos[curso_id]
        return curso
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado!")


@app.post('/cursos', status_code=status.HTTP_201_CREATED, response_model=Curso)
async def post_curso(curso: Curso, db: Any = Depends(fake_db)):
    next_id: int = len(cursos) + 1
    # cursos[next_id] = curso
    # del curso.id
    curso.id = next_id
    cursos.append(curso)
    
    return curso


@app.put('/cursos/{curso_id}')
async def put_curso(curso_id: int, curso: Curso, db: Any = Depends(fake_db)):
    if curso_id in cursos:
        cursos[curso_id] = curso
        curso.id = curso_id
        del curso.id

        return curso
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Não existe um curos o id {curso_id}")


@app.delete('/cursos/{curso_id}')
async def delete_curso(curso_id: int, db: Any = Depends(fake_db)):
    if curso_id in cursos:
        del cursos[curso_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
        # -------------------------------------------------------------------------------------------------
        # return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)                                    *
        # O JSONResponse tem um bug nessa versão do FastAPI                                              *
        # -------------------------------------------------------------------------------------------------
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Não existe um curso com o id {curso_id}")


@app.get('/calculadora')
# ---------------------------------------------------------------------------------------------------------
# Query parameters: 18 Prática Query Parameters_720p                                                      *
# ---------------------------------------------------------------------------------------------------------
async def calcular(a: int = Query(default=None, gt=5), b: int = Query(default=None, gt=10), x_geek: str = Header(default=None), c: Optional[int] = None):
    soma: int = a + b
    if c:
        soma = soma + c

    print('X-GEEK:', x_geek)

    return {"resultado": soma}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0.",
                port=8000, debug=True, reload=True)

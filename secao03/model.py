from typing import Optional

from pydantic import BaseModel


class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int


cursos = [
    Curso(id=1, titulo="Programação em Python", aulas=112, horas=58),
    Curso(id=2, titulo="Programação em Python Avançado", aulas=150, horas=60),
]

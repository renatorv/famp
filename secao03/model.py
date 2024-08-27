from typing import Optional

from pydantic import BaseModel, validator


class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int  # mais de 12 aulas
    horas: int  # mais de 10 aulas

    @validator('horas')
    def valida_horas(cls, value):
        if value < 10:
            raise ValueError('O curso deve ter no mínimo 10 horas.')
        return value

    @validator('aulas')
    def valida_aulas(cls, value):
        if value < 12:
            raise ValueError('O curso deve ter no mínimo 12 aulas.')
        return value

    @validator('titulo')
    def validar_titulo(cls, value):
        palavras = value.split(' ')
        # Validação 1
        if len(palavras) < 3:
            raise ValueError(
                'O título do curso deve ter no mínimo 3 palavras.')

        # Validação 2
        if value.islower():
            raise ValueError('O título do deve ser capitalizado.')
        return value


cursos = [
    Curso(id=1, titulo="Programação em Python", aulas=112, horas=58),
    Curso(id=2, titulo="Programação em Python Avançado", aulas=150, horas=60),
]

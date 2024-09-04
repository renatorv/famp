from typing import Optional
# pois o sqlalchemy tbm tem um BaseModel
from pydantic import BaseModel as SCBaseModel
"""
Para cada model deve existir um schema correspondente, em se tratando de API's.

    É possível criar vários schemas para um mesmo model, dependendo da necessidade da API.
    Ex:
        class CursoSchemaReduzido(SCBaseModel):
        titulo: str
        aulas: int

        class Config:
            orm_mode = True
"""


class CursoSchema(SCBaseModel):
    id: Optional[int]
    titulo: str
    aulas: int
    horas: int

    class Config:
        orm_mode = True

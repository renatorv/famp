from core.configs import settings
from sqlalchemy import Column, Integer, String


class CursoModel(settings.DBBaseModel):
    """
        Classe modelo para a tabela curso
    """
    __tablename__ = "cursos"

    id: int = Column(Integer, primary_key=True, index=True, autoincrement=True)
    titulo: str = Column(String(100), nullable=False)
    aulas: str = Column(Integer, nullable=False)
    horas: int = Column(Integer, nullable=False)

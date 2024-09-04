from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    """
        Configurações gerais do projeto
    """
    API_V1_STR: str = "/api/v1"
    DB_URL: str = "postgresql+asyncpg://renato:159753@localhost:5432/faculdade"
    DBBaseModel = declarative_base()

    class Config:
        case_sensitive = True

        """
            Instância da classe Settings
            para que a classe Settings possa se instânciada em qq lugar da aplicação
            e assim temos acessos a essas configurações.
        """


settings = Settings()

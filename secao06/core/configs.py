from typing import List
from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    DB_URL: str = "postgresql+asyncpg://renato:159753@localhost:5432/faculdade"
    DBBaseModel = declarative_base()
    
    JWT_SECRET: str = '0t0wN2NAhR8QuOrrAxCwslP_RWjux7bXWnlPIbl6EcQ'
    """
        abrir o terminal e digitar o comando abaixo
        
        python [no terminal]
        
        import secrets
        
        token: str = secrets.token_urlsafe(32)
        
        token
        
        exit()
    """
    ALGORITHM: str = 'HS256'
    # 60 minutes * 24 hours * 7 days = 1 SEMANA
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7 # 1 week

    class Config:
        case_sensitive = True


settings: Settings = Settings()
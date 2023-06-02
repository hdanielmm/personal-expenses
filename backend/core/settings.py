from pydantic import BaseSettings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    db_server: str  # db_hostname
    db_port: str
    db_user: str
    db_password: str
    db_name: str
    secret_key: str
    algorithm: str
    #access_token_expire_minutes: str

    class Config:
        env_file = ".env"


settings = Settings()

SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.db_user}:{settings.db_password}@{settings.db_server}/{settings.db_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autflush=False, bind=engine)

Base = declarative_base()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

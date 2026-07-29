"""
backend/database/connection.py
---------------------------------------------------------
LOTERIAS MATRIX PLATFORM

Conexão com PostgreSQL

Versão: 1.2
"""

import os

from urllib.parse import quote_plus

from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


load_dotenv()


DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


PASSWORD_ENCODED = quote_plus(DB_PASSWORD)


DATABASE_URL = (
    f"postgresql+psycopg://"
    f"{DB_USER}:{PASSWORD_ENCODED}@"
    f"{DB_HOST}:{DB_PORT}/"
    f"{DB_NAME}"
)


engine = create_engine(
    DATABASE_URL,
    echo=False,
    future=True
)


SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    future=True
)


Base = declarative_base()


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()
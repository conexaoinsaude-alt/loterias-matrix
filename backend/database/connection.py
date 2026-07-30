"""
backend/database/connection.py
---------------------------------------------------------
LOTERIAS MATRIX PLATFORM

Conexão com PostgreSQL

Versão: 2.0
"""

import os
from urllib.parse import quote_plus

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

# ==========================================================
# PRIORIDADE 1: DATABASE_URL (Render)
# ==========================================================

DATABASE_URL = os.getenv("DATABASE_URL")

# ==========================================================
# PRIORIDADE 2: Variáveis individuais (.env / ambiente local)
# ==========================================================

if not DATABASE_URL:

    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT", "5432")
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "")

    PASSWORD_ENCODED = quote_plus(DB_PASSWORD)

    DATABASE_URL = (
        f"postgresql+psycopg://"
        f"{DB_USER}:{PASSWORD_ENCODED}@"
        f"{DB_HOST}:{DB_PORT}/"
        f"{DB_NAME}"
    )

# ==========================================================
# Compatibilidade com SQLAlchemy
# ==========================================================

if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace(
        "postgres://",
        "postgresql+psycopg://",
        1
    )

elif DATABASE_URL.startswith("postgresql://"):
    DATABASE_URL = DATABASE_URL.replace(
        "postgresql://",
        "postgresql+psycopg://",
        1
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
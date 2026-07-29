"""
backend/models/user.py
---------------------------------------------------------
LOTERIAS MATRIX PLATFORM

Modelo ORM de Usuário

Versão: 1.1

Responsabilidades:

- Representar usuários da plataforma.
- Mapear tabela users no PostgreSQL.
- Definir estrutura ORM com SQLAlchemy.
"""

from datetime import datetime

from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String

from backend.database.connection import Base


class User(Base):

    __tablename__ = "users"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    username = Column(
        String(100),
        nullable=False
    )


    email = Column(
        String(255),
        unique=True,
        index=True,
        nullable=False
    )


    password_hash = Column(
        String(255),
        nullable=False
    )


    active = Column(
        Boolean,
        default=True
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )
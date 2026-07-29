"""
backend/database/init_db.py
---------------------------------------------------------
LOTERIAS MATRIX PLATFORM

Inicialização do Banco de Dados

Versão: 1.0

Responsabilidades:

- Criar tabelas ORM no PostgreSQL.
- Carregar todos os modelos.
- Executar criação da estrutura inicial.
"""

from backend.database.connection import Base
from backend.database.connection import engine

# Importa os modelos para registrar as tabelas no ORM
from backend.models.user import User


def create_tables():

    Base.metadata.create_all(bind=engine)

    print("DATABASE TABLES CREATED")


if __name__ == "__main__":

    create_tables()
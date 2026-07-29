"""
backend/config.py
---------------------------------------------------------
LOTERIAS MATRIX PLATFORM

Configurações do Backend

Versão: 1.0

Responsabilidades:

- Centralizar configurações da plataforma.
- Definir informações da aplicação.
- Configurar CORS.
- Preparar ambiente para desenvolvimento e produção.
"""

from pathlib import Path


# Diretório raiz do projeto
BASE_DIR = Path(__file__).resolve().parent.parent


# Informações da aplicação
APP_NAME = "LOTERIAS MATRIX PLATFORM"

APP_VERSION = "1.0.0"

API_PREFIX = "/api"


# Ambientes
ENVIRONMENT = "development"

DEBUG = True


# CORS
ALLOWED_ORIGINS = [
    "*"
]


# Diretórios do projeto
DATASETS_DIR = BASE_DIR / "datasets"

OUTPUTS_DIR = BASE_DIR / "outputs"

DATABASE_DIR = BASE_DIR / "database"


# Banco de dados (será utilizado nas próximas etapas)
DATABASE_URL = (
    "postgresql://postgres:postgres@localhost:5432/loterias_matrix"
)
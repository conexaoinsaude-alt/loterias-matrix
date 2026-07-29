"""
backend/main.py
---------------------------------------------------------
LOTERIAS MATRIX PLATFORM

Backend Principal

Versão: 1.5

Responsabilidades:

- Inicializar a API.
- Configurar servidor FastAPI.
- Registrar rotas da plataforma.
- Disponibilizar endpoints principais.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.routers import system
from backend.routers import users
from backend.routers import generator
from backend.routers import statistics
from backend.routers import ai


app = FastAPI(

    title="LOTERIAS MATRIX PLATFORM",

    description="API Oficial da Plataforma LOTERIAS MATRIX",

    version="1.5.0"

)


app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]

)


# Registro das rotas do sistema

app.include_router(system.router)


# Registro das rotas de usuários

app.include_router(users.router)


# Registro das rotas do gerador

app.include_router(generator.router)


# Registro das rotas de estatísticas

app.include_router(statistics.router)


# Registro das rotas de Inteligência Artificial

app.include_router(ai.router)


@app.get("/")

def home():

    return {

        "platform": "LOTERIAS MATRIX PLATFORM",

        "status": "ONLINE",

        "version": "1.5.0",

        "modules": [

            "System",

            "Users",

            "Generator",

            "Statistics",

            "AI Loterias"

        ]

    }
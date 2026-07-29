"""
backend/main.py
---------------------------------------------------------
LOTERIAS MATRIX PLATFORM

Backend Principal

Versão: 1.4

Responsabilidades:

- Inicializar a API.
- Configurar servidor FastAPI.
- Registrar todos os módulos.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.routers import system
from backend.routers import users
from backend.routers import generator
from backend.routers import statistics


app = FastAPI(

    title="LOTERIAS MATRIX PLATFORM",

    description="API Oficial da Plataforma LOTERIAS MATRIX",

    version="1.4.0"

)


app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]

)


# ==========================================================
# ROTAS
# ==========================================================

app.include_router(system.router)

app.include_router(users.router)

app.include_router(generator.router)

app.include_router(statistics.router)


# ==========================================================
# HOME
# ==========================================================

@app.get("/")

def home():

    return {

        "platform": "LOTERIAS MATRIX PLATFORM",

        "status": "ONLINE",

        "version": "1.4.0",

        "modules": [

            "System",

            "Users",

            "Generator",

            "Statistics"

        ]

    }
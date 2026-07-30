"""
backend/main.py
---------------------------------------------------------
LOTERIAS MATRIX PLATFORM

Backend Principal

Versão: 1.6

Responsabilidades:

- Inicializar API.
- Configurar servidor FastAPI.
- Registrar rotas.
- Servir interface frontend.
"""

from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

from backend.routers import system
from backend.routers import users
from backend.routers import generator
from backend.routers import statistics
from backend.routers import ai


BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = BASE_DIR / "frontend"


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


# Rotas da plataforma

app.include_router(system.router)

app.include_router(users.router)

app.include_router(generator.router)

app.include_router(statistics.router)

app.include_router(ai.router)



# Interface Web

@app.get("/")
def home():

    index_file = FRONTEND_DIR / "index.html"

    return FileResponse(index_file)
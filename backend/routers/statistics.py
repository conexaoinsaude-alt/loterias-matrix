"""
backend/routers/statistics.py
---------------------------------------------------------
LOTERIAS MATRIX PLATFORM

API - Estatísticas

Versão: 1.0

Responsabilidades:

- Disponibilizar estatísticas da plataforma.
- Expor informações do AI Statistical Engine.
- Disponibilizar resumo estatístico.
"""

from fastapi import APIRouter

router = APIRouter(

    prefix="/statistics",

    tags=["Estatísticas"]

)


@router.get("/")

def statistics_information():

    return {

        "module": "LOTERIAS MATRIX STATISTICS",

        "status": "READY",

        "version": "1.0.0",

        "description": "Módulo Estatístico da Plataforma"

    }


@router.get("/health")

def health():

    return {

        "status": "ONLINE"

    }


@router.get("/summary")

def summary():

    return {

        "status": "READY",

        "message": "Resumo estatístico disponível.",

        "features": [

            "Frequência",

            "Probabilidade",

            "Atraso",

            "Ranking",

            "AI Statistical Engine",

            "Paridade",

            "Faixas",

            "Exportação"

        ]

    }
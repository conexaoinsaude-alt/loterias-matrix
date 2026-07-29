"""
backend/routers/system.py
---------------------------------------------------------
LOTERIAS MATRIX PLATFORM

Rotas do Sistema

Versão: 1.0

Responsabilidades:

- Informações da plataforma.
- Status da API.
- Health Check.
- Versão do sistema.
"""

from datetime import datetime

from fastapi import APIRouter


router = APIRouter(

    prefix="/system",

    tags=["Sistema"]

)


@router.get("/")

def system_information():

    return {

        "platform": "LOTERIAS MATRIX PLATFORM",

        "version": "1.0.0",

        "status": "ONLINE",

        "server_time": datetime.now().isoformat()

    }


@router.get("/health")

def health():

    return {

        "status": "OK",

        "service": "API",

        "timestamp": datetime.now().isoformat()

    }


@router.get("/version")

def version():

    return {

        "name": "LOTERIAS MATRIX PLATFORM",

        "version": "1.0.0"

    }
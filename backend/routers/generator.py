"""
backend/routers/generator.py
---------------------------------------------------------
LOTERIAS MATRIX PLATFORM

API - Gerador Inteligente

Versão: 1.3

Responsabilidades:

- Disponibilizar o Gerador pela API.
- Receber parâmetros do Frontend.
- Chamar o motor matemático.
- Retornar jogos gerados.
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from engine import LotteryEngine
from config import LOTTERIES


router = APIRouter(
    prefix="/generator",
    tags=["Generator"]
)


class GeneratorRequest(BaseModel):

    loteria: str

    quantidade_jogos: int = 5



@router.get("/")
def generator_information():

    return {

        "module": "LOTERIAS MATRIX GENERATOR",

        "status": "READY",

        "version": "1.3.0",

        "description": "Motor Inteligente de Geração de Jogos"

    }



@router.get("/health")
def health():

    return {

        "status": "ONLINE"

    }



@router.post("/create")
def create_games(request: GeneratorRequest):

    try:

        if request.loteria not in LOTTERIES:

            raise HTTPException(
                status_code=400,
                detail="Loteria não suportada"
            )


        configuracao = LOTTERIES[request.loteria]


        arquivo_csv = (
            f"datasets/{request.loteria}.csv"
        )


        engine = LotteryEngine(

            arquivo_csv,

            configuracao["max_num"],

            configuracao["draw_numbers"]

        )


        resultado = engine.executar(

            request.quantidade_jogos

        )


        return {

            "status": "success",

            "loteria": request.loteria,

            "resultado": resultado

        }


    except HTTPException:

        raise


    except Exception as erro:

        raise HTTPException(

            status_code=500,

            detail=str(erro)

        )
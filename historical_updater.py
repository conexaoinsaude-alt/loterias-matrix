"""
historical_updater.py
---------------------------------------------------------
LOTERIAS MATRIX

Atualizador de Históricos

Versão: 2.0

Responsabilidades:

- Controlar atualização dos datasets.
- Verificar integridade dos arquivos.
- Preparar sincronização futura.
"""

from pathlib import Path
from datetime import datetime

from exceptions import DatasetError



class HistoricalUpdater:


    def __init__(
        self,
        directory="datasets"
    ):

        self.directory = Path(
            directory
        )

        self.directory.mkdir(
            exist_ok=True
        )



    def localizar_dataset(
        self,
        loteria
    ):

        return (
            self.directory
            /
            f"{loteria}.csv"
        )



    def verificar_status(
        self,
        loteria
    ):

        arquivo = self.localizar_dataset(
            loteria
        )


        if not arquivo.exists():

            return {
                "status": "missing",
                "arquivo": str(arquivo)
            }



        tamanho = arquivo.stat().st_size



        if tamanho == 0:

            return {
                "status": "empty",
                "arquivo": str(arquivo)
            }



        return {

            "status": "available",

            "arquivo": str(arquivo),

            "tamanho_bytes": tamanho,

            "atualizado_em":
                datetime.fromtimestamp(
                    arquivo.stat().st_mtime
                ).isoformat()

        }



    def validar_dataset(
        self,
        loteria
    ):

        status = self.verificar_status(
            loteria
        )


        if status["status"] != "available":

            raise DatasetError(
                f"Dataset inválido: {status}"
            )


        return True
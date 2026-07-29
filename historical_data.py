"""
historical_data.py
---------------------------------------------------------
LOTERIAS MATRIX

Gerenciador de Históricos

Versão: 2.0

Responsabilidades:

- Controlar arquivos históricos.
- Validar datasets.
- Preparar importação futura.
"""

from pathlib import Path

from exceptions import DatasetError



class HistoricalDataManager:


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



    def caminho_dataset(
        self,
        loteria
    ):

        return (
            self.directory
            /
            f"{loteria}.csv"
        )



    def verificar_dataset(
        self,
        loteria
    ):

        arquivo = self.caminho_dataset(
            loteria
        )


        if not arquivo.exists():

            raise DatasetError(
                f"Dataset não encontrado: {arquivo}"
            )


        if arquivo.stat().st_size == 0:

            raise DatasetError(
                f"Dataset vazio: {arquivo}"
            )


        return arquivo



    def listar_datasets(
        self
    ):

        return [
            arquivo.stem
            for arquivo in self.directory.glob(
                "*.csv"
            )
        ]



    def criar_dataset_vazio(
        self,
        loteria
    ):

        arquivo = self.caminho_dataset(
            loteria
        )


        arquivo.touch()


        return arquivo
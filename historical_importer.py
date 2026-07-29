"""
historical_importer.py
---------------------------------------------------------
LOTERIAS MATRIX

Importador de Históricos

Versão: 2.0

Responsabilidades:

- Importar arquivos CSV de históricos.
- Validar estrutura básica.
- Organizar datasets.
"""

from pathlib import Path
import shutil

from exceptions import DatasetError



class HistoricalImporter:


    def __init__(
        self,
        destination="datasets"
    ):

        self.destination = Path(
            destination
        )

        self.destination.mkdir(
            exist_ok=True
        )



    def validar_arquivo(
        self,
        arquivo
    ):

        caminho = Path(
            arquivo
        )


        if not caminho.exists():

            raise DatasetError(
                f"Arquivo não encontrado: {arquivo}"
            )


        if caminho.stat().st_size == 0:

            raise DatasetError(
                f"Arquivo vazio: {arquivo}"
            )


        if caminho.suffix.lower() != ".csv":

            raise DatasetError(
                "Somente arquivos CSV são aceitos."
            )


        return True



    def importar(
        self,
        arquivo,
        nome_loteria
    ):

        self.validar_arquivo(
            arquivo
        )


        destino = (
            self.destination
            /
            f"{nome_loteria}.csv"
        )


        shutil.copy2(
            arquivo,
            destino
        )


        return destino
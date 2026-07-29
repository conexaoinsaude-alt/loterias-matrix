"""
data_manager.py
---------------------------------------------------------
LOTERIAS MATRIX

Gerenciador de Dados

Versão: 2.0

Responsabilidades:

- Controlar localização dos datasets.
- Verificar existência dos históricos.
- Integrar validação dos arquivos.
- Preparar integração com importadores.
"""

from pathlib import Path

from validator import (
    DatasetValidator,
    DatasetValidationError
)


class DataManager:

    def __init__(self, base_directory="datasets"):

        self.base_directory = Path(
            base_directory
        )

        self.base_directory.mkdir(
            exist_ok=True
        )


    def caminho_dataset(
        self,
        nome_loteria
    ):

        return (
            self.base_directory
            / f"{nome_loteria}.csv"
        )


    def validar_dataset(
        self,
        nome_loteria,
        quantidade_dezenas
    ):

        arquivo = self.caminho_dataset(
            nome_loteria
        )

        validator = DatasetValidator(
            str(arquivo),
            quantidade_dezenas
        )

        try:

            return validator.validar()

        except DatasetValidationError as erro:

            print(
                "\nERRO NA VALIDAÇÃO DO DATASET:"
            )

            print(erro)

            return None


    def possui_dataset(
        self,
        nome_loteria
    ):

        arquivo = self.caminho_dataset(
            nome_loteria
        )

        return arquivo.exists()
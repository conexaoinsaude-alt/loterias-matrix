"""
validator.py
---------------------------------------------------------
LOTERIAS MATRIX

Validador de Datasets

Versão: 2.0

Responsabilidades:

- Verificar se o arquivo existe.
- Verificar se o arquivo está vazio.
- Validar cabeçalhos.
- Validar quantidade de colunas.
- Validar valores nulos.
- Carregar o DataFrame validado.

Autor:
LOTERIAS MATRIX
"""

from pathlib import Path

import pandas as pd


class DatasetValidationError(Exception):
    """Erro específico para validação de datasets."""
    pass


class DatasetValidator:

    def __init__(self, csv_path: str, quantidade_dezenas: int):

        self.csv_path = Path(csv_path)
        self.quantidade_dezenas = quantidade_dezenas

    def validar(self) -> pd.DataFrame:

        if not self.csv_path.exists():

            raise DatasetValidationError(
                f"Arquivo não encontrado:\n{self.csv_path}"
            )

        if self.csv_path.stat().st_size == 0:

            raise DatasetValidationError(
                f"O arquivo está vazio:\n{self.csv_path}"
            )

        try:

            df = pd.read_csv(self.csv_path)

        except Exception as erro:

            raise DatasetValidationError(
                f"Erro ao ler o arquivo:\n{erro}"
            )

        colunas_esperadas = [
            f"num{i}"
            for i in range(
                1,
                self.quantidade_dezenas + 1
            )
        ]

        colunas_faltando = [
            coluna
            for coluna in colunas_esperadas
            if coluna not in df.columns
        ]

        if colunas_faltando:

            raise DatasetValidationError(
                "Colunas obrigatórias ausentes:\n"
                + ", ".join(colunas_faltando)
            )

        if df.empty:

            raise DatasetValidationError(
                "O dataset não possui concursos."
            )

        if df[colunas_esperadas].isnull().any().any():

            raise DatasetValidationError(
                "Foram encontrados valores vazios nas dezenas."
            )

        return df
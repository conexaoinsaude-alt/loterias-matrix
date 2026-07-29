"""
normalizer.py
---------------------------------------------------------
LOTERIAS MATRIX

Normalizador de Dados

Versão: 2.0

Responsabilidades:

- Padronizar nomes das colunas.
- Garantir formato num1, num2, num3...
- Preparar dados para a matriz estatística.
"""

import pandas as pd


class DataNormalizer:

    def __init__(self, quantidade_dezenas: int):

        self.quantidade_dezenas = quantidade_dezenas


    def normalizar(
        self,
        df: pd.DataFrame
    ) -> pd.DataFrame:
        """
        Converte diferentes formatos para
        o padrão interno do LOTERIAS MATRIX.
        """

        df = df.copy()

        novas_colunas = {}

        for indice in range(
            1,
            self.quantidade_dezenas + 1
        ):

            encontrados = [
                coluna
                for coluna in df.columns
                if str(coluna).lower()
                in [
                    f"num{indice}",
                    f"bola{indice}",
                    f"dezena{indice}",
                    f"numero{indice}"
                ]
            ]

            if encontrados:

                novas_colunas[
                    encontrados[0]
                ] = f"num{indice}"


        df = df.rename(
            columns=novas_colunas
        )


        colunas_finais = [
            f"num{i}"
            for i in range(
                1,
                self.quantidade_dezenas + 1
            )
        ]


        df = df[
            colunas_finais
        ]


        return df
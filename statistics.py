"""
statistics.py
---------------------------------------------------------
LOTERIAS MATRIX

Módulo de Estatística Avançada

Versão: 2.0

Responsabilidades:

- Gerar ranking de dezenas.
- Identificar dezenas quentes.
- Identificar dezenas frias.
- Analisar atrasos.
- Produzir indicadores estatísticos.
"""

import pandas as pd


class StatisticalAnalyzer:

    def __init__(
        self,
        matriz: pd.DataFrame
    ):

        self.matriz = matriz.copy()


    def ranking_frequencia(self):

        return (
            self.matriz
            .sort_values(
                by="Frequencia",
                ascending=False
            )
            .reset_index(
                drop=True
            )
        )


    def dezenas_quentes(
        self,
        quantidade=10
    ):

        return (
            self.ranking_frequencia()
            .head(quantidade)
        )


    def dezenas_frias(
        self,
        quantidade=10
    ):

        return (
            self.matriz
            .sort_values(
                by="Frequencia",
                ascending=True
            )
            .head(quantidade)
            .reset_index(
                drop=True
            )
        )


    def maiores_atrasos(
        self,
        quantidade=10
    ):

        return (
            self.matriz
            .sort_values(
                by="Atraso",
                ascending=False
            )
            .head(quantidade)
            .reset_index(
                drop=True
            )
        )


    def resumo(self):

        return {

            "total_dezenas":
                len(self.matriz),

            "maior_frequencia":
                int(
                    self.matriz[
                        "Frequencia"
                    ].max()
                ),

            "maior_atraso":
                int(
                    self.matriz[
                        "Atraso"
                    ].max()
                ),

            "media_frequencia":
                float(
                    self.matriz[
                        "Frequencia"
                    ].mean()
                )
        }
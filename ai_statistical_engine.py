"""
ai_statistical_engine.py
---------------------------------------------------------
LOTERIAS MATRIX

AI Statistical Engine

Versão: 1.0

Responsabilidades:

- Receber matriz estatística base.
- Calcular indicadores avançados.
- Criar score estatístico.
- Gerar ranking inteligente.
- Preparar dados para o gerador.

Observação:

Este módulo realiza análise estatística.
Não prevê resultados garantidos.
"""

import numpy as np
import pandas as pd


class AIStatisticalEngine:


    def __init__(
        self,
        matriz: pd.DataFrame
    ):

        self.matriz = matriz.copy()


        self.resultado = None



    def validar_matriz(self):

        obrigatorias = [

            "Numero",
            "Frequencia",
            "Atraso",
            "Probabilidade"

        ]


        faltantes = [

            coluna

            for coluna in obrigatorias

            if coluna not in self.matriz.columns

        ]


        if faltantes:

            raise ValueError(
                f"Colunas ausentes na matriz: {faltantes}"
            )


        return True



    def calcular_frequencia_normalizada(self):

        maior = self.matriz["Frequencia"].max()


        if maior == 0:

            self.matriz[
                "Frequencia_Normalizada"
            ] = 0


        else:

            self.matriz[
                "Frequencia_Normalizada"
            ] = (

                self.matriz["Frequencia"]
                /
                maior

            )


        return self.matriz



    def calcular_atraso_normalizado(self):

        maior = self.matriz["Atraso"].max()


        if maior == 0:

            self.matriz[
                "Atraso_Normalizado"
            ] = 0


        else:

            self.matriz[
                "Atraso_Normalizado"
            ] = (

                self.matriz["Atraso"]
                /
                maior

            )


        return self.matriz



    def calcular_recencia(self):

        self.matriz[
            "Indice_Recencia"
        ] = (

            1
            -
            self.matriz["Atraso_Normalizado"]

        )


        return self.matriz



    def calcular_equilibrio_estatistico(self):

        self.matriz[
            "Equilibrio_Estatistico"
        ] = (

            self.matriz[
                "Frequencia_Normalizada"
            ]
            *
            0.6

            +

            self.matriz[
                "Indice_Recencia"
            ]
            *
            0.4

        )


        return self.matriz



    def calcular_score_estatistico(self):

        self.matriz[
            "Score_Estatistico"
        ] = (

            self.matriz[
                "Frequencia_Normalizada"
            ]
            *
            0.35

            +

            self.matriz[
                "Indice_Recencia"
            ]
            *
            0.25

            +

            self.matriz[
                "Probabilidade"
            ]
            *
            0.25

            +

            self.matriz[
                "Equilibrio_Estatistico"
            ]
            *
            0.15

        )


        self.matriz[
            "Score_Estatistico"
        ] = (

            self.matriz[
                "Score_Estatistico"
            ]
            .round(8)

        )


        return self.matriz



    def calcular_ranking(self):

        self.matriz = (

            self.matriz
            .sort_values(

                by="Score_Estatistico",

                ascending=False

            )

            .reset_index(
                drop=True
            )

        )


        self.matriz[
            "Ranking"
        ] = np.arange(

            1,

            len(self.matriz) + 1

        )


        return self.matriz



    def analisar_faixas(self):

        self.matriz[
            "Faixa_Numero"
        ] = (

            (
                self.matriz["Numero"]
                -
                1
            )

            //

            10

            +

            1

        )


        return self.matriz



    def analisar_paridade(self):

        self.matriz[
            "Paridade"
        ] = (

            self.matriz[
                "Numero"
            ]

            .apply(

                lambda numero:

                "PAR"

                if numero % 2 == 0

                else

                "IMPAR"

            )

        )


        return self.matriz



    def gerar_resumo(self):

        ranking = (

            self.matriz
            .sort_values(

                by="Score_Estatistico",

                ascending=False

            )

        )


        return {

            "numeros_quentes":

                ranking
                .head(10)
                [
                    "Numero"
                ]
                .tolist(),


            "numeros_atrasados":

                self.matriz
                .sort_values(

                    by="Atraso",

                    ascending=False

                )
                .head(10)
                [
                    "Numero"
                ]
                .tolist(),


            "melhores_scores":

                ranking
                .head(10)
                [
                    "Score_Estatistico"
                ]
                .tolist()

        }



    def executar_analise(self):

        self.validar_matriz()

        self.calcular_frequencia_normalizada()

        self.calcular_atraso_normalizado()

        self.calcular_recencia()

        self.calcular_equilibrio_estatistico()

        self.calcular_score_estatistico()

        self.calcular_ranking()

        self.analisar_faixas()

        self.analisar_paridade()


        self.resultado = self.matriz.copy()


        return self.resultado
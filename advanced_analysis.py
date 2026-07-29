"""
advanced_analysis.py
---------------------------------------------------------
LOTERIAS MATRIX

Análise Estatística Avançada

Versão: 2.0

Responsabilidades:

- Analisar matriz estatística.
- Identificar números quentes.
- Identificar números atrasados.
- Gerar indicadores.
"""

import pandas as pd



class AdvancedAnalyzer:


    def __init__(
        self,
        matriz: pd.DataFrame
    ):

        self.matriz = matriz



    def numeros_quentes(
        self,
        quantidade=10
    ):

        resultado = (

            self.matriz

            .sort_values(

                by="Frequencia",

                ascending=False

            )

            .head(quantidade)

        )


        return resultado[
            "Numero"
        ].tolist()



    def numeros_atrasados(
        self,
        quantidade=10
    ):

        resultado = (

            self.matriz

            .sort_values(

                by="Atraso",

                ascending=False

            )

            .head(quantidade)

        )


        return resultado[
            "Numero"
        ].tolist()



    def melhores_probabilidades(
        self,
        quantidade=10
    ):

        resultado = (

            self.matriz

            .sort_values(

                by="Probabilidade",

                ascending=False

            )

            .head(quantidade)

        )


        return resultado[
            "Numero"
        ].tolist()



    def resumo(
        self
    ):

        return {

            "numeros_quentes":

                self.numeros_quentes(),


            "numeros_atrasados":

                self.numeros_atrasados(),


            "melhores_probabilidades":

                self.melhores_probabilidades()

        }
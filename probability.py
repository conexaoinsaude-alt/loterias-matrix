"""
probability.py
---------------------------------------------------------
LOTERIAS MATRIX

Motor Probabilístico

Versão: 2.1

Responsabilidades:

- Trabalhar com pesos estatísticos.
- Selecionar dezenas candidatas.
- Normalizar probabilidades.
- Preparar base para geração inteligente.
"""

import numpy as np
import pandas as pd


class ProbabilityEngine:


    def __init__(
        self,
        matriz: pd.DataFrame
    ):

        self.matriz = matriz.copy()



    def obter_probabilidades(self):

        probabilidades = (
            self.matriz["Probabilidade"]
            .astype(float)
            .to_numpy()
        )


        probabilidades = np.nan_to_num(
            probabilidades,
            nan=0.0,
            posinf=0.0,
            neginf=0.0
        )


        probabilidades[
            probabilidades < 0
        ] = 0



        soma = probabilidades.sum()


        if soma <= 0:

            return np.ones(
                len(probabilidades)
            ) / len(probabilidades)



        probabilidades = (
            probabilidades / soma
        )


        probabilidades = (
            probabilidades /
            probabilidades.sum()
        )


        return probabilidades



    def ranking_probabilidade(self):

        return (
            self.matriz
            .sort_values(
                by="Probabilidade",
                ascending=False
            )
            .reset_index(
                drop=True
            )
        )



    def selecionar_dezenas(
        self,
        quantidade
    ):

        numeros = (
            self.matriz["Numero"]
            .to_numpy()
        )


        probabilidades = (
            self.obter_probabilidades()
        )


        selecionadas = np.random.choice(
            numeros,
            size=quantidade,
            replace=False,
            p=probabilidades
        )


        return sorted(
            selecionadas.tolist()
        )
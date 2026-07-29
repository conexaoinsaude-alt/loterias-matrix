"""
generator.py
---------------------------------------------------------
LOTERIAS MATRIX

Gerador Inteligente de Combinações

Versão 3.0

Responsabilidades:

- Receber matriz estatística.
- Utilizar probabilidade histórica.
- Utilizar Score Estatístico AI.
- Criar peso inteligente.
- Gerar combinações probabilísticas.
"""

import numpy as np
import pandas as pd



def calcular_peso_inteligente(
    matriz: pd.DataFrame
):

    dados = matriz.copy()



    if "Score_Estatistico" in dados.columns:


        probabilidade = (

            dados["Probabilidade"]
            .astype(float)

        )


        score = (

            dados["Score_Estatistico"]
            .astype(float)

        )



        peso = (

            probabilidade
            *
            0.40

            +

            score
            *
            0.60

        )


    else:


        peso = (

            dados["Probabilidade"]
            .astype(float)

        )



    peso = np.nan_to_num(

        peso.to_numpy(),

        nan=0.0,

        posinf=0.0,

        neginf=0.0

    )



    peso[peso < 0] = 0



    soma = peso.sum()



    if soma <= 0:

        peso = (

            np.ones(
                len(peso)
            )
            /
            len(peso)

        )


    else:

        peso = (

            peso
            /
            soma

        )



    return peso





def gerar_combinacoes(
    matriz: pd.DataFrame,
    quantidade_jogos: int,
    quantidade_dezenas: int,
    max_num: int
):


    probabilidades = calcular_peso_inteligente(

        matriz

    )



    numeros = np.arange(

        1,

        max_num + 1

    )



    jogos = []



    for _ in range(
        quantidade_jogos
    ):


        jogo = []



        while len(jogo) < quantidade_dezenas:


            numero = np.random.choice(

                numeros,

                p=probabilidades

            )



            if numero not in jogo:

                jogo.append(

                    int(numero)

                )



        jogo.sort()



        jogos.append(

            jogo

        )



    return jogos





def salvar_jogos(
    jogos,
    arquivo_saida
):


    df = pd.DataFrame(

        jogos

    )


    df.to_csv(

        arquivo_saida,

        index=False,

        header=False,

        encoding="utf-8-sig"

    )
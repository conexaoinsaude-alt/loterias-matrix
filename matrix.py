"""
matrix.py
---------------------------------------------------------
LOTERIAS MATRIX

Constrói a Matriz Estatística de Probabilidade.

Versão 2.0

Responsabilidades:

- Carregar histórico.
- Validar dados de entrada.
- Construir matriz estatística.
- Calcular frequência.
- Calcular atraso.
- Calcular peso probabilístico.
"""

from pathlib import Path

import pandas as pd
import numpy as np

from exceptions import DatasetError



def carregar_historico(
    csv_path: str,
    quantidade_dezenas: int
) -> pd.DataFrame:
    """
    Carrega o histórico da loteria.
    """

    arquivo = Path(csv_path)


    if not arquivo.exists():

        raise DatasetError(
            f"Arquivo não encontrado: {csv_path}"
        )


    if arquivo.stat().st_size == 0:

        raise DatasetError(
            f"O arquivo histórico está vazio: {csv_path}"
        )


    try:

        df = pd.read_csv(
            arquivo
        )

    except Exception as erro:

        raise DatasetError(
            f"Erro ao ler histórico: {erro}"
        )



    colunas = [
        f"num{i}"
        for i in range(
            1,
            quantidade_dezenas + 1
        )
    ]


    faltantes = [
        coluna
        for coluna in colunas
        if coluna not in df.columns
    ]


    if faltantes:

        raise DatasetError(
            f"Colunas ausentes no histórico: {faltantes}"
        )



    df["numeros"] = (
        df[colunas]
        .values
        .tolist()
    )


    return df




def construir_matriz(
    df: pd.DataFrame,
    max_num: int,
    quantidade_dezenas: int
) -> pd.DataFrame:
    """
    Constrói a matriz estatística.
    """


    frequencia = np.zeros(
        max_num + 1
    )


    ultima_aparicao = {

        numero: -1

        for numero in range(
            1,
            max_num + 1
        )
    }


    total_concursos = len(df)



    for indice, linha in df.iterrows():

        dezenas = linha["numeros"]


        for numero in dezenas:

            frequencia[numero] += 1

            ultima_aparicao[numero] = indice



    atraso = np.zeros(
        max_num + 1
    )


    for numero in range(
        1,
        max_num + 1
    ):

        if ultima_aparicao[numero] == -1:

            atraso[numero] = total_concursos

        else:

            atraso[numero] = (
                total_concursos
                -
                ultima_aparicao[numero]
            )



    frequencia_relativa = (
        frequencia
        /
        max(total_concursos, 1)
    )



    peso = frequencia * (
        1 +
        atraso /
        max(total_concursos, 1)
    )



    probabilidade = np.zeros(
        max_num
    )


    soma_peso = peso[1:].sum()


    if soma_peso > 0:

        probabilidade = (
            peso[1:]
            /
            soma_peso
        )



    matriz = pd.DataFrame({

        "Numero":
            range(
                1,
                max_num + 1
            ),

        "Frequencia":
            frequencia[1:].astype(int),

        "Frequencia_Relativa":
            np.round(
                frequencia_relativa[1:],
                6
            ),

        "Atraso":
            atraso[1:].astype(int),

        "Peso":
            np.round(
                peso[1:],
                6
            ),

        "Probabilidade":
            np.round(
                probabilidade,
                8
            )

    })


    return matriz
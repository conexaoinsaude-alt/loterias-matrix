"""
dataset_builder.py
---------------------------------------------------------
LOTERIAS MATRIX

Construtor de Datasets

Versão 2.0

Responsabilidades:

- Criar estrutura dos históricos.
- Padronizar colunas CSV.
- Preparar arquivos para análise.
"""

from pathlib import Path

import pandas as pd



class DatasetBuilder:


    def __init__(
        self,
        directory="datasets"
    ):

        self.directory = Path(
            directory
        )

        self.directory.mkdir(
            exist_ok=True
        )



    def criar_cabecalho(
        self,
        quantidade_dezenas
    ):

        return [

            f"num{i}"

            for i in range(

                1,

                quantidade_dezenas + 1

            )

        ]



    def criar_dataset(
        self,
        loteria,
        quantidade_dezenas
    ):

        arquivo = (

            self.directory

            /

            f"{loteria}.csv"

        )


        colunas = self.criar_cabecalho(
            quantidade_dezenas
        )


        df = pd.DataFrame(
            columns=colunas
        )


        df.to_csv(

            arquivo,

            index=False,

            encoding="utf-8-sig"

        )


        return arquivo



    def validar_estrutura(
        self,
        arquivo,
        quantidade_dezenas
    ):

        caminho = Path(
            arquivo
        )


        if not caminho.exists():

            return False



        df = pd.read_csv(
            caminho
        )


        esperado = self.criar_cabecalho(
            quantidade_dezenas
        )


        return list(
            df.columns
        ) == esperado
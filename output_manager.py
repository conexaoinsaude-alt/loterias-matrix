"""
output_manager.py
---------------------------------------------------------
LOTERIAS MATRIX

Gerenciador de Saídas

Versão: 2.0

Responsabilidades:

- Criar estrutura de resultados.
- Salvar jogos gerados.
- Salvar matrizes.
- Salvar relatórios.
- Organizar arquivos do sistema.
"""

from pathlib import Path
from datetime import datetime

import pandas as pd


class OutputManager:


    def __init__(
        self,
        directory="outputs"
    ):

        self.directory = Path(
            directory
        )

        self.directory.mkdir(
            exist_ok=True
        )


    def criar_subpasta_execucao(self):

        nome = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )


        pasta = (
            self.directory
            / nome
        )


        pasta.mkdir(
            exist_ok=True
        )


        return pasta



    def salvar_jogos(
        self,
        jogos,
        pasta
    ):

        arquivo = (
            pasta
            / "jogos_gerados.csv"
        )


        df = pd.DataFrame(
            jogos
        )


        df.to_csv(
            arquivo,
            index=False,
            header=False,
            encoding="utf-8-sig"
        )


        return arquivo



    def salvar_matriz(
        self,
        matriz,
        pasta
    ):

        arquivo = (
            pasta
            / "matriz_estatistica.csv"
        )


        matriz.to_csv(
            arquivo,
            index=False,
            encoding="utf-8-sig"
        )


        return arquivo



    def salvar_relatorio(
        self,
        relatorio,
        pasta
    ):

        arquivo = (
            pasta
            / "relatorio.json"
        )


        import json


        with open(
            arquivo,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                relatorio,
                f,
                indent=4,
                ensure_ascii=False
            )


        return arquivo
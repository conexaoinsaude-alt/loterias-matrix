"""
importer.py
---------------------------------------------------------
LOTERIAS MATRIX

Importador de históricos de loterias.

Versão 2.0

Responsabilidades:

- Receber dados de concursos.
- Padronizar estrutura.
- Salvar datasets em CSV.
- Preparar integração futura com APIs.
"""

from pathlib import Path

import pandas as pd


class LotteryImporter:

    def __init__(self, output_directory="datasets"):

        self.output_directory = Path(output_directory)

        self.output_directory.mkdir(
            exist_ok=True
        )


    def salvar_csv(
        self,
        dados,
        nome_loteria
    ):
        """
        Salva histórico da loteria em CSV.
        """

        arquivo = (
            self.output_directory
            / f"{nome_loteria}.csv"
        )

        df = pd.DataFrame(dados)

        df.to_csv(
            arquivo,
            index=False,
            encoding="utf-8-sig"
        )

        return arquivo


    def importar_lista(
        self,
        concursos,
        nome_loteria
    ):
        """
        Importa uma lista de concursos
        e salva no padrão do projeto.
        """

        if not concursos:

            raise ValueError(
                "Nenhum concurso informado."
            )

        arquivo = self.salvar_csv(
            concursos,
            nome_loteria
        )

        return arquivo


    def informar_status(
        self,
        arquivo
    ):

        print("=" * 60)
        print("IMPORTAÇÃO CONCLUÍDA")
        print("=" * 60)
        print(
            f"Arquivo criado: {arquivo}"
        )
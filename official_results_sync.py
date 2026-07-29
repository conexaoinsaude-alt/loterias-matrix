"""
official_results_sync.py
---------------------------------------------------------
LOTERIAS MATRIX

Sincronizador Oficial de Resultados

Versão: 1.0

Responsabilidades:

- Coordenar atualização dos datasets.
- Validar arquivos de entrada.
- Integrar HistoricalImporter.
- Integrar HistoricalUpdater.
- Preparar sincronização automática futura.
"""

from pathlib import Path
from datetime import datetime

from historical_importer import HistoricalImporter
from historical_updater import HistoricalUpdater


class OfficialResultsSync:

    def __init__(self, datasets_directory="datasets"):

        self.datasets_directory = Path(datasets_directory)

        self.datasets_directory.mkdir(
            exist_ok=True
        )

        self.importer = HistoricalImporter(
            destination=datasets_directory
        )

        self.updater = HistoricalUpdater(
            directory=datasets_directory
        )

    def status(self, loteria):

        return self.updater.verificar_status(
            loteria
        )

    def importar_csv(
        self,
        arquivo_csv,
        loteria
    ):

        self.importer.importar(
            arquivo_csv,
            loteria
        )

        return self.status(
            loteria
        )

    def sincronizar(
        self,
        arquivo_csv,
        loteria
    ):

        antes = self.status(
            loteria
        )

        self.importar_csv(
            arquivo_csv,
            loteria
        )

        depois = self.status(
            loteria
        )

        return {

            "sucesso": True,
            "loteria": loteria,
            "antes": antes,
            "depois": depois,
            "sincronizado_em": datetime.now().isoformat()

        }

    def sincronizar_todos(
        self,
        arquivos
    ):

        resultados = {}

        for loteria, arquivo in arquivos.items():

            try:

                resultados[loteria] = self.sincronizar(
                    arquivo,
                    loteria
                )

            except Exception as erro:

                resultados[loteria] = {

                    "sucesso": False,
                    "erro": str(erro)

                }

        return resultados


if __name__ == "__main__":

    print("OfficialResultsSync carregado com sucesso.")
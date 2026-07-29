"""
official_results_provider.py
---------------------------------------------------------
LOTERIAS MATRIX

Provedor Oficial de Resultados

Versão: 1.0

Responsabilidades:

- Definir uma interface única para provedores.
- Validar provedores disponíveis.
- Registrar provedores.
- Permitir expansão futura.
"""

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Dict, List


class OfficialResultsProvider(ABC):
    """
    Interface base para qualquer provedor de resultados.
    """

    @property
    @abstractmethod
    def provider_name(self) -> str:
        pass

    @abstractmethod
    def available_lotteries(self) -> List[str]:
        pass

    @abstractmethod
    def fetch(self, lottery: str):
        """
        Retorna os resultados da loteria solicitada.

        O retorno deverá ser uma lista de registros ou
        um DataFrame, dependendo da implementação do
        provedor concreto.
        """
        pass


class LocalCSVProvider(OfficialResultsProvider):
    """
    Provedor baseado em arquivos CSV locais.

    Nesta primeira versão ele apenas localiza e valida
    os arquivos. Futuramente poderá realizar validações
    avançadas.
    """

    def __init__(self, datasets_directory="datasets"):

        self.datasets_directory = Path(
            datasets_directory
        )

    @property
    def provider_name(self):

        return "Local CSV"

    def available_lotteries(self):

        return sorted(

            arquivo.stem

            for arquivo in self.datasets_directory.glob(
                "*.csv"
            )

        )

    def fetch(
        self,
        lottery
    ):

        arquivo = (
            self.datasets_directory
            /
            f"{lottery}.csv"
        )

        if not arquivo.exists():

            raise FileNotFoundError(

                f"Dataset não encontrado: {arquivo}"

            )

        return arquivo


class ProviderRegistry:
    """
    Registro de provedores disponíveis.
    """

    def __init__(self):

        self._providers: Dict[
            str,
            OfficialResultsProvider
        ] = {}

    def register(
        self,
        provider: OfficialResultsProvider
    ):

        self._providers[
            provider.provider_name
        ] = provider

    def names(self):

        return sorted(

            self._providers.keys()

        )

    def get(
        self,
        provider_name
    ):

        if provider_name not in self._providers:

            raise ValueError(

                f"Provedor não registrado: {provider_name}"

            )

        return self._providers[
            provider_name
        ]


def build_default_registry():

    registry = ProviderRegistry()

    registry.register(

        LocalCSVProvider()

    )

    return registry


if __name__ == "__main__":

    registry = build_default_registry()

    print("Provedores registrados:")

    for nome in registry.names():

        print(f"- {nome}")
"""
exceptions.py
---------------------------------------------------------
LOTERIAS MATRIX

Exceções Personalizadas do Sistema

Versão: 2.0

Responsabilidades:

- Padronizar erros internos.
- Facilitar tratamento no aplicativo.
- Separar falhas de dados, configuração
  e processamento.
"""


class LotteriasMatrixError(Exception):
    """
    Erro base do sistema.
    """

    pass



class DatasetError(
    LotteriasMatrixError
):
    """
    Erros relacionados aos arquivos
    de histórico.
    """

    pass



class ConfigurationError(
    LotteriasMatrixError
):
    """
    Erros de configuração das loterias.
    """

    pass



class ProcessingError(
    LotteriasMatrixError
):
    """
    Erros durante processamento
    estatístico.
    """

    pass



class GenerationError(
    LotteriasMatrixError
):
    """
    Erros durante geração
    de combinações.
    """

    pass
"""
logger.py
---------------------------------------------------------
LOTERIAS MATRIX

Sistema de Logs

Versão: 2.0

Responsabilidades:

- Registrar operações do sistema.
- Registrar erros.
- Criar histórico de execução.
- Facilitar auditoria do software.
"""

from pathlib import Path
from datetime import datetime


class SystemLogger:


    def __init__(
        self,
        log_directory="logs"
    ):

        self.log_directory = Path(
            log_directory
        )

        self.log_directory.mkdir(
            exist_ok=True
        )

        self.log_file = (
            self.log_directory
            / "lotterias_matrix.log"
        )



    def registrar(
        self,
        mensagem,
        nivel="INFO"
    ):

        data = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )


        linha = (
            f"[{data}] "
            f"[{nivel}] "
            f"{mensagem}\n"
        )


        with open(
            self.log_file,
            "a",
            encoding="utf-8"
        ) as arquivo:

            arquivo.write(
                linha
            )



    def info(
        self,
        mensagem
    ):

        self.registrar(
            mensagem,
            "INFO"
        )



    def erro(
        self,
        mensagem
    ):

        self.registrar(
            mensagem,
            "ERROR"
        )



    def sucesso(
        self,
        mensagem
    ):

        self.registrar(
            mensagem,
            "SUCCESS"
        )
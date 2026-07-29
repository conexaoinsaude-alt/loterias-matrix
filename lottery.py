"""
lottery.py
---------------------------------------------------------
LOTERIAS MATRIX

Gerenciador de Regras das Loterias

Versão: 2.0

Responsabilidades:

- Controlar configurações específicas.
- Validar parâmetros da modalidade.
- Preparar expansão para novas loterias.
"""

from dataclasses import dataclass


@dataclass
class LotteryRule:

    nome: str

    max_num: int

    quantidade_dezenas: int



class LotteryManager:


    def __init__(
        self,
        configuracao
    ):

        self.configuracao = configuracao



    def obter_regra(
        self,
        chave
    ):

        dados = self.configuracao.get(
            chave
        )


        if not dados:

            raise ValueError(
                f"Loteria não encontrada: {chave}"
            )


        return LotteryRule(

            nome=dados.get(
                "nome",
                chave
            ),

            max_num=dados.get(
                "max_num",
                0
            ),

            quantidade_dezenas=dados.get(
                "draw_numbers",
                0
            )
        )



    def listar_loterias(self):

        return list(
            self.configuracao.keys()
        )
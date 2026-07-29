"""
LOTERIAS MATRIX 2026

Recommendation Engine

Arquivo:
backend/services/recommendation_engine.py

Responsabilidade:

Motor de recomendações estatísticas
da IA Loterias.

Não prevê resultados.

Gera orientações baseadas em:
- Score estatístico
- Tendências
- Equilíbrio par/ímpar
- Distribuição de faixas
"""


class RecommendationEngine:
    """
    Motor responsável por gerar
    recomendações estatísticas.
    """


    def __init__(
        self,
        score=None,
        tendencias=None,
        equilibrio=None,
        distribuicao=None
    ):

        self.score = score or {}

        self.tendencias = tendencias or {}

        self.equilibrio = equilibrio or {}

        self.distribuicao = distribuicao or {}



    def recomendar_dezenas_prioritarias(
        self,
        quantidade=10
    ):
        """
        Retorna dezenas com maior pontuação.
        """

        ranking = sorted(
            self.score.items(),
            key=lambda item: item[1],
            reverse=True
        )


        return [

            numero

            for numero, valor in ranking[:quantidade]

        ]



    def recomendar_equilibrio(self):
        """
        Analisa equilíbrio estatístico.
        """

        if not self.equilibrio:

            return {

                "status":
                    "sem_dados"

            }


        return {

            "pares":

                self.equilibrio.get(
                    "percentual_par",
                    0
                ),


            "impares":

                self.equilibrio.get(
                    "percentual_impar",
                    0
                ),


            "orientacao":

                "Manter equilíbrio próximo ao histórico."

        }



    def recomendar_faixas(self):
        """
        Analisa distribuição das dezenas.
        """

        return {

            "distribuicao":

                self.distribuicao,


            "orientacao":

                "Evitar concentração excessiva em uma única faixa."

        }



    def recomendar_tendencias(self):
        """
        Analisa tendências recentes.
        """

        return {

            "numeros_em_alta":

                self.tendencias.get(
                    "numeros_em_alta",
                    []
                ),


            "numeros_em_baixa":

                self.tendencias.get(
                    "numeros_em_baixa",
                    []
                ),


            "orientacao":

                "Usar tendências apenas como indicador estatístico."

        }



    def resumo_recomendacoes(self):
        """
        Retorna resumo completo das recomendações.
        """

        return {

            "dezenas_prioritarias":

                self.recomendar_dezenas_prioritarias(),


            "equilibrio":

                self.recomendar_equilibrio(),


            "faixas":

                self.recomendar_faixas(),


            "tendencias":

                self.recomendar_tendencias(),


            "observacao":

                "Recomendações baseadas em análise histórica estatística."

        }



    def gerar_recomendacao(self):
        """
        Compatibilidade com API IA Loterias.

        Método chamado pelo arquivo:
        backend/routers/ai.py
        """

        return self.resumo_recomendacoes()
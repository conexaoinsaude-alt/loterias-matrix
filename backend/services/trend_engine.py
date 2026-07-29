"""
LOTERIAS MATRIX 2026

Trend Engine

Arquivo:
backend/services/trend_engine.py

Responsabilidade:

Motor inicial de análise de tendências
da IA Loterias.

Não prevê resultados.

Analisa comportamento histórico
das dezenas.
"""


from collections import Counter



class TrendEngine:
    """
    Motor responsável por analisar
    tendências estatísticas.
    """


    def __init__(self, historico=None):

        self.historico = historico or []



    def frequencia_recente(self, quantidade_concursos=3):
        """
        Analisa frequência dos concursos
        mais recentes.
        """

        concursos = self.historico[-quantidade_concursos:]

        contador = Counter()


        for concurso in concursos:

            for numero in concurso:

                contador[numero] += 1


        return dict(
            sorted(
                contador.items(),
                key=lambda item: item[1],
                reverse=True
            )
        )



    def numeros_em_alta(self, limite=3):
        """
        Identifica dezenas com maior
        ocorrência recente.
        """

        frequencia = self.frequencia_recente()


        return list(
            frequencia.keys()
        )[:limite]



    def numeros_em_baixa(self, limite=3):
        """
        Identifica dezenas com menor
        ocorrência recente.
        """

        frequencia = self.frequencia_recente()


        return list(
            reversed(
                list(frequencia.keys())
            )
        )[:limite]



    def comparativo_recente_historico(self):

        """
        Compara frequência geral
        com frequência recente.
        """

        geral = Counter()


        recente = Counter(
            self.frequencia_recente()
        )


        for concurso in self.historico:

            for numero in concurso:

                geral[numero] += 1



        resultado = {}


        for numero in geral:

            resultado[numero] = {

                "historico":
                    geral[numero],

                "recente":
                    recente.get(
                        numero,
                        0
                    )

            }


        return resultado



    def resumo_tendencia(self):

        return {

            "frequencia_recente":
                self.frequencia_recente(),

            "numeros_em_alta":
                self.numeros_em_alta(),

            "numeros_em_baixa":
                self.numeros_em_baixa(),

            "comparativo":
                self.comparativo_recente_historico()

        }
"""
LOTERIAS MATRIX 2026

AI Score Engine

Arquivo:
backend/services/score_engine.py

Responsabilidade:

Motor inicial de pontuação estatística
da IA Loterias.

Este módulo NÃO prevê resultados.

Ele classifica dezenas através
de indicadores estatísticos.
"""


class ScoreEngine:
    """
    Motor responsável pelo cálculo
    do score estatístico.
    """


    def __init__(self, frequencias=None):

        self.frequencias = frequencias or {}


    def normalizar_frequencia(self):
        """
        Converte frequência absoluta
        em pontuação percentual.
        """

        if not self.frequencias:

            return {}


        maior_valor = max(
            self.frequencias.values()
        )


        if maior_valor == 0:

            return {}


        scores = {}


        for numero, frequencia in self.frequencias.items():

            scores[numero] = round(
                (frequencia / maior_valor) * 100,
                2
            )


        return scores



    def ranking_score(self):
        """
        Retorna ranking das dezenas
        pelo score estatístico.
        """

        scores = self.normalizar_frequencia()


        return dict(
            sorted(
                scores.items(),
                key=lambda item: item[1],
                reverse=True
            )
        )



    def classificar_numeros(self):
        """
        Classificação inicial:

        Alto:
        score >= 70

        Médio:
        score >= 40

        Baixo:
        abaixo de 40
        """

        ranking = self.ranking_score()


        resultado = {

            "alto": [],

            "medio": [],

            "baixo": []

        }


        for numero, score in ranking.items():


            if score >= 70:

                resultado["alto"].append(
                    numero
                )


            elif score >= 40:

                resultado["medio"].append(
                    numero
                )


            else:

                resultado["baixo"].append(
                    numero
                )


        return resultado



    def resumo_score(self):

        return {

            "score_numeros":
                self.ranking_score(),

            "classificacao":
                self.classificar_numeros()

        }
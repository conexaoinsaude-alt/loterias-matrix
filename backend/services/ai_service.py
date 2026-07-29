"""
LOTERIAS MATRIX 2026

AI Statistical Engine

Arquivo:
backend/services/ai_service.py

Responsabilidade:

Motor estatístico inicial da IA Loterias.

Este módulo NÃO prevê resultados.

Ele analisa dados históricos
e gera indicadores estatísticos.
"""


from collections import Counter


class AIStatisticalEngine:
    """
    Motor principal de análise estatística.
    """

    def __init__(self, historico=None):

        self.historico = historico or []


    def frequencia_numeros(self):
        """
        Calcula frequência histórica
        das dezenas.
        """

        contador = Counter()

        for concurso in self.historico:

            for numero in concurso:

                contador[numero] += 1


        return dict(
            sorted(
                contador.items(),
                key=lambda item: item[1],
                reverse=True
            )
        )


    def numeros_quentes(self, quantidade=10):
        """
        Retorna números
        com maior frequência.
        """

        frequencia = self.frequencia_numeros()

        return list(
            frequencia.keys()
        )[:quantidade]


    def numeros_frios(self, quantidade=10):
        """
        Retorna números
        com menor frequência.
        """

        frequencia = self.frequencia_numeros()

        return list(
            reversed(
                list(frequencia.keys())
            )
        )[:quantidade]


    def equilibrio_par_impar(self):
        """
        Analisa proporção
        de pares e ímpares.
        """

        pares = 0
        impares = 0


        for concurso in self.historico:

            for numero in concurso:

                if numero % 2 == 0:
                    pares += 1

                else:
                    impares += 1


        total = pares + impares


        if total == 0:

            return {

                "pares": 0,

                "impares": 0,

                "percentual_par": 0,

                "percentual_impar": 0

            }


        return {

            "pares": pares,

            "impares": impares,

            "percentual_par":
                round(
                    (pares / total) * 100,
                    2
                ),

            "percentual_impar":
                round(
                    (impares / total) * 100,
                    2
                )

        }


    def distribuicao_faixas(self):
        """
        Divide números por faixas.
        """

        faixas = {

            "01-05": 0,

            "06-10": 0,

            "11-15": 0,

            "16-20": 0,

            "21-25": 0

        }


        for concurso in self.historico:

            for numero in concurso:


                if 1 <= numero <= 5:

                    faixas["01-05"] += 1


                elif 6 <= numero <= 10:

                    faixas["06-10"] += 1


                elif 11 <= numero <= 15:

                    faixas["11-15"] += 1


                elif 16 <= numero <= 20:

                    faixas["16-20"] += 1


                elif 21 <= numero <= 25:

                    faixas["21-25"] += 1


        return faixas


    def resumo_executivo(self):

        return {

            "frequencia_historica":
                self.frequencia_numeros(),

            "numeros_quentes":
                self.numeros_quentes(),

            "numeros_frios":
                self.numeros_frios(),

            "equilibrio_par_impar":
                self.equilibrio_par_impar(),

            "distribuicao_faixas":
                self.distribuicao_faixas()

        }
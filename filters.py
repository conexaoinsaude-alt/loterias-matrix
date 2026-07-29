"""
filters.py
---------------------------------------------------------
LOTERIAS MATRIX

Motor de Filtros Matemáticos

Versão: 2.0

Responsabilidades:

- Filtrar combinações geradas.
- Controlar pares e ímpares.
- Controlar soma das dezenas.
- Controlar distribuição numérica.
- Evitar padrões extremos.
"""

from typing import List


class CombinationFilter:


    def __init__(
        self,
        soma_minima=None,
        soma_maxima=None,
        pares_minimo=None,
        pares_maximo=None
    ):

        self.soma_minima = soma_minima
        self.soma_maxima = soma_maxima

        self.pares_minimo = pares_minimo
        self.pares_maximo = pares_maximo



    def validar_soma(
        self,
        jogo: List[int]
    ):

        soma = sum(jogo)

        if self.soma_minima:

            if soma < self.soma_minima:
                return False


        if self.soma_maxima:

            if soma > self.soma_maxima:
                return False


        return True



    def validar_pares(
        self,
        jogo: List[int]
    ):

        quantidade_pares = len(
            [
                numero
                for numero in jogo
                if numero % 2 == 0
            ]
        )


        if self.pares_minimo is not None:

            if quantidade_pares < self.pares_minimo:
                return False


        if self.pares_maximo is not None:

            if quantidade_pares > self.pares_maximo:
                return False


        return True



    def validar_sequencia(
        self,
        jogo: List[int],
        limite=3
    ):

        sequencia = 1


        for i in range(
            1,
            len(jogo)
        ):

            if jogo[i] == jogo[i-1] + 1:

                sequencia += 1

                if sequencia >= limite:

                    return False

            else:

                sequencia = 1


        return True



    def validar(
        self,
        jogo: List[int]
    ):

        if not self.validar_soma(jogo):

            return False


        if not self.validar_pares(jogo):

            return False


        if not self.validar_sequencia(jogo):

            return False


        return True



    def aplicar(
        self,
        jogos
    ):

        return [
            jogo
            for jogo in jogos
            if self.validar(jogo)
        ]
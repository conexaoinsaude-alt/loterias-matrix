"""
config.py
---------------------------------------------------------
Configurações das loterias suportadas pelo projeto
LOTERIAS MATRIX
"""

LOTTERIES = {

    "mega_sena": {
        "nome": "Mega-Sena",
        "max_num": 60,
        "draw_numbers": 6
    },


    "lotofacil": {

        "nome": "Lotofácil",

        # Quantidade sorteada oficialmente
        "draw_numbers": 15,

        # Menor aposta permitida
        "min_bet_numbers": 15,

        # Maior aposta permitida
        "max_bet_numbers": 20,

        # Total de dezenas existentes
        "max_num": 25

    },


    "quina": {
        "nome": "Quina",
        "max_num": 80,
        "draw_numbers": 5
    },


    "lotomania": {
        "nome": "Lotomania",
        "max_num": 100,
        "draw_numbers": 50
    },


    "timemania": {
        "nome": "Timemania",
        "max_num": 80,
        "draw_numbers": 7
    },


    "dia_de_sorte": {
        "nome": "Dia de Sorte",
        "max_num": 31,
        "draw_numbers": 7
    },


    "mais_milionaria": {
        "nome": "+Milionária",
        "max_num": 50,
        "draw_numbers": 6,
        "trevos": 2
    },


    "super_sete": {
        "nome": "Super Sete",
        "max_num": 10,
        "draw_numbers": 7
    }

}
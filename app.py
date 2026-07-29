"""
app.py
---------------------------------------------------------
LOTERIAS MATRIX

Versão 2.0

Interface principal do sistema.

Responsabilidades:

- Exibir menu das loterias.
- Receber escolha do usuário.
- Acionar o LotteryEngine.
- Exibir resultados.
"""

from pathlib import Path

from config import LOTTERIES
from lottery import LotteryManager
from engine import LotteryEngine
from exceptions import LotteriasMatrixError


BASE_DIR = Path(__file__).resolve().parent

DATASETS_DIR = BASE_DIR / "datasets"



def main():

    print("=" * 60)
    print("LOTERIAS MATRIX")
    print("=" * 60)


    try:

        manager = LotteryManager(
            LOTTERIES
        )


        loterias = manager.listar_loterias()


        print("\nLoterias disponíveis:\n")


        for indice, chave in enumerate(
            loterias,
            start=1
        ):

            regra = manager.obter_regra(
                chave
            )

            print(
                f"{indice} - {regra.nome}"
            )


        opcao = int(
            input(
                "\nEscolha a loteria: "
            )
        )


        chave = loterias[
            opcao - 1
        ]


        regra = manager.obter_regra(
            chave
        )


        arquivo_csv = (
            DATASETS_DIR
            / f"{chave}.csv"
        )


        if not arquivo_csv.exists():

            print(
                "\nArquivo histórico não encontrado:"
            )

            print(
                arquivo_csv
            )

            return


        quantidade = int(
            input(
                "\nQuantidade de jogos para gerar: "
            )
        )


        print(
            "\nExecutando análise..."
        )


        sistema = LotteryEngine(

            str(arquivo_csv),

            regra.max_num,

            regra.quantidade_dezenas

        )


        resultado = sistema.executar(
            quantidade
        )


        print(
            "\nJogos gerados:\n"
        )


        for jogo in resultado["jogos"]:

            print(
                jogo
            )


        print(
            "\nResumo estatístico:"
        )

        print(
            resultado["relatorio"]
        )


        print(
            "\nProcessamento concluído."
        )


    except LotteriasMatrixError as erro:

        print(
            "\nErro do sistema:"
        )

        print(
            erro
        )


    except Exception as erro:

        print(
            "\nErro inesperado:"
        )

        print(
            erro
        )



if __name__ == "__main__":

    main()
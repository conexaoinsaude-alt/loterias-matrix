"""
engine.py
---------------------------------------------------------
LOTERIAS MATRIX

Motor Principal de Análise

Versão 3.0

Responsabilidades:

- Executar fluxo completo.
- Carregar histórico.
- Construir matriz estatística.
- Executar AI Statistical Engine.
- Executar análise avançada.
- Gerar jogos.
- Criar relatórios.
"""

from matrix import (
    carregar_historico,
    construir_matriz
)


from generator import (
    gerar_combinacoes
)


from advanced_analysis import (
    AdvancedAnalyzer
)


from ai_statistical_engine import (
    AIStatisticalEngine
)


from reports import (
    criar_relatorio
)


from output_manager import (
    OutputManager
)



class LotteryEngine:


    def __init__(
        self,
        arquivo_csv,
        max_num,
        quantidade_dezenas
    ):

        self.arquivo_csv = arquivo_csv

        self.max_num = max_num

        self.quantidade_dezenas = quantidade_dezenas



    def executar(
        self,
        quantidade_jogos
    ):


        df = carregar_historico(

            self.arquivo_csv,

            self.quantidade_dezenas

        )



        matriz = construir_matriz(

            df,

            self.max_num,

            self.quantidade_dezenas

        )



        ai_engine = AIStatisticalEngine(

            matriz

        )


        matriz = ai_engine.executar_analise()



        analise = AdvancedAnalyzer(

            matriz

        )


        resumo = analise.resumo()



        resumo_ai = ai_engine.gerar_resumo()



        resumo.update(

            {

                "ai_statistical_engine":

                    resumo_ai

            }

        )



        jogos = gerar_combinacoes(

            matriz,

            quantidade_jogos,

            self.quantidade_dezenas,

            self.max_num

        )



        output = OutputManager()



        pasta = output.criar_subpasta_execucao()



        arquivo_matriz = output.salvar_matriz(

            matriz,

            pasta

        )



        arquivo_jogos = output.salvar_jogos(

            jogos,

            pasta

        )



        arquivo_relatorio = output.salvar_relatorio(

            criar_relatorio(

                resumo

            ),

            pasta

        )



        return {


            "jogos":

                jogos,


            "relatorio":

                resumo,


            "arquivos": {


                "matriz":

                    str(arquivo_matriz),


                "jogos":

                    str(arquivo_jogos),


                "relatorio":

                    str(arquivo_relatorio)

            }

        }
const API_URL = "http://127.0.0.1:8000";


let ultimoResultado = "";



document.addEventListener("DOMContentLoaded", () => {

    carregarStatus();

    inicializarMenu();

    restaurarConfiguracoes();

});



async function carregarStatus() {

    try {

        const response = await fetch(API_URL);


        if (!response.ok) {

            throw new Error();

        }


        const data = await response.json();


        document.getElementById("status").textContent =
            data.status;


        document.getElementById("version").textContent =
            data.version;


        document.getElementById("api-status").textContent =
            "🟢 API ONLINE";


    }

    catch {


        document.getElementById("status").textContent =
            "OFFLINE";


        document.getElementById("version").textContent =
            "--";


        document.getElementById("api-status").textContent =
            "🔴 API OFFLINE";


    }

}





function inicializarMenu() {


    document.querySelectorAll(".sidebar li")
    .forEach(item => {


        item.addEventListener("click", function () {


            document.querySelectorAll(".sidebar li")
            .forEach(menu => {

                menu.classList.remove("active");

            });


            this.classList.add("active");


        });


    });


}





function restaurarConfiguracoes() {


    const loteria =
        localStorage.getItem("loteriaSelecionada");


    const quantidade =
        localStorage.getItem("quantidadeJogos");



    if (loteria) {


        document.getElementById("loteria").value =
            loteria;


    }



    if (quantidade) {


        document.getElementById("quantidade-jogos").value =
            quantidade;


    }



    const resultadoSalvo =
        localStorage.getItem("ultimoResultado");



    if (resultadoSalvo) {


        document.getElementById("resultado-gerador")
        .textContent =
            resultadoSalvo;


        ultimoResultado = resultadoSalvo;


    }


}





async function gerarJogos() {


    const resultado =
        document.getElementById("resultado-gerador");



    const selectLoteria =
        document.getElementById("loteria");



    const selectQuantidade =
        document.getElementById("quantidade-jogos");



    const loteria =
        selectLoteria.value;



    const quantidade =
        parseInt(
            selectQuantidade.value
        );



    localStorage.setItem(
        "loteriaSelecionada",
        loteria
    );



    localStorage.setItem(
        "quantidadeJogos",
        quantidade
    );



    resultado.textContent =
        "⏳ Gerando jogos...";



    try {



        const response = await fetch(

            `${API_URL}/generator/create`,

            {

                method: "POST",


                headers: {

                    "Content-Type": "application/json"

                },


                body: JSON.stringify({

                    loteria: loteria,

                    quantidade_jogos: quantidade

                })

            }

        );



        const data =
            await response.json();




        if (!response.ok) {


            throw new Error(
                data.detail ||
                "Erro ao gerar jogos."
            );


        }




        if (
            !data.resultado ||
            !data.resultado.jogos ||
            data.resultado.jogos.length === 0
        ) {


            throw new Error(
                "Nenhum jogo foi gerado pelo motor."
            );


        }




        let texto = "";



        texto +=
            "🎯 LOTERIAS MATRIX PLATFORM\n";


        texto +=
            "====================================\n\n";


        texto +=
            "Loteria: "
            + data.loteria
            + "\n";


        texto +=
            "Quantidade: "
            + quantidade
            + "\n\n";




        data.resultado.jogos.forEach(

            (jogo, indice) => {


                texto +=
                    `Jogo ${indice + 1}\n`;


                texto +=
                    jogo.join(" - ");


                texto +=
                    "\n\n";


            }

        );




        ultimoResultado = texto;



        localStorage.setItem(

            "ultimoResultado",

            texto

        );



        resultado.textContent =
            ultimoResultado;



    }



    catch (erro) {


        console.error(erro);



        resultado.textContent =
            "ERRO:\n\n"
            + erro.message;


    }


}
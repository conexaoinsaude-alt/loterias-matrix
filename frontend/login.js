const API_URL = "http://127.0.0.1:8000";


const form = document.getElementById("login-form");


if (form) {


    form.addEventListener("submit", async function(event) {


        event.preventDefault();


        const email = document.getElementById("email").value;

        const password = document.getElementById("password").value;


        const message = document.getElementById("login-message");



        try {


            const response = await fetch(
                `${API_URL}/users/login`,
                {

                    method: "POST",

                    headers: {

                        "Content-Type": "application/json"

                    },

                    body: JSON.stringify({

                        email: email,

                        password: password

                    })

                }
            );



            const data = await response.json();



            if(response.ok){


                message.textContent =
                "Login realizado com sucesso";


                localStorage.setItem(
                    "user",
                    JSON.stringify(data.user)
                );


                setTimeout(()=>{

                    window.location.href="index.html";

                },1000);


            }

            else{


                message.textContent =
                data.detail || "Usuário ou senha inválidos";


            }



        }

        catch(error){


            message.textContent =
            "Erro ao conectar com servidor";


            console.error(error);


        }



    });


}
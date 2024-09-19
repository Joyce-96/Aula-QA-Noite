const user = "teste@teste.com";
const senha = "123456";

function logar() {
  let emailInput = document.getElementById("email").value;
  let senhaInput = document.getElementById("senha").value;

  if (emailInput === user && senhaInput === senha) {
    window.location.assign('https://www.google.com')
  } else {
    console.log("Não logado");
  }
}

const button = document.getElementById("button-entrar");

button.addEventListener("click", logar);

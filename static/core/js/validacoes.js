/**
 * VALIDAÇÕES DE LOGIN E CADASTRO
 */
function validarNome(){
    nome = document.getElementById('nome');
    nome.style.border = '1px solid red';
    nome.style.backgroundColor = 'white';
    nome.focus();
}

function validarCpf(){
    cpf = document.getElementById('cpf');
    cpf.style.border = '1px solid red';
    cpf.style.backgroundColor = 'white';
    cpf.focus();
}

function validarEndereco(){
    endereco = document.getElementById('endereco');
    endereco.style.border = '1px solid red';
    endereco.style.backgroundColor = 'white';
    endereco.focus();
}

function validarTelefone(){
    telefone = document.getElementById('telefone');
    telefone.style.border = '1px solid red';
    telefone.style.backgroundColor = 'white';
    telefone.focus();
}


function validarUsuario(){
    username = document.getElementById('username');
    username.style.border = '1px solid red';
    username.style.backgroundColor = 'white';
    username.focus();
}

function validarSenha(){
    senha = document.getElementById('senha');
    senha.style.border = '1px solid red';
    senha.style.backgroundColor = 'white';
    senha.focus();
}

function validarEmail(){
    email = document.getElementById('email');
    email.style.border = '1px solid red';
    email.style.backgroundColor = 'white';
    email.focus();
}

var displayHora = document.getElementById('time');

function horaAtual() {
  var hora = new Date();
  var h = hora.getHours(); 
  var m = hora.getMinutes();
  var horaFormatada = (h + ":" + m);
  displayHora.innerHTML = horaFormatada;
}

setInterval(horaAtual, 1000);
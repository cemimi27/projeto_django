from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_django, logout as logout_django
from django.contrib.auth.decorators import login_required
from core.models import Usuario
from time import sleep


def login(request):
    pagina_atual = request.get_full_path().split("/")[2]
    if pagina_atual == "login":
        link = "Cadastro"

    if request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        if len(username) == 0:
            return render(request, 'login.html', {'error_username': 'Campo usuário obrigatório!', 'pagina_atual': link})
        elif len(senha) == 0:
            return render(request, 'login.html', {'error_senha': 'Campo senha obrigatório!',  'pagina_atual': link})
        else:
            resultado = validarLoginModel(request, username, senha)
            if resultado == 'Sucesso':
                return render(request, 'login.html', {'msg_success': 'Sucesso'})
            else:
                return resultado
    else:
        return render(request, 'login.html', {'pagina_atual': link})

def validarLoginModel(request, username, senha):
    user = authenticate(username=username, password=senha)
    if user:
        login_django(request, user)
        return redirect('../home')
    else:
        return render(request, 'login.html', {'error_banco': 'Usuário ou senha inválidos!'})


def cadastro(request):
    pagina_atual = request.get_full_path().split("/")[2]
    if pagina_atual == "cadastro":
        link = "Login"

    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        endereco = request.POST.get('endereco')
        telefone = request.POST.get('telefone')
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        
        dados = {'nome': nome, 'cpf': cpf, 'endereco': endereco, 'telefone': telefone, 'username': 
        username, 'email': email, 'senha': senha}
        

        for d in dados:
            if len(dados[d]) == 0:
                if d == 'endereco':
                    return render(request, 'cadastro.html', {f'error_{d}': f'Campo endereço obrigatório!', 'pagina_atual': link})
                elif d == 'username':
                    return render(request, 'cadastro.html', {f'error_{d}': f'Campo usuário obrigatório!', 'pagina_atual': link})
                else:
                    return render(request, 'cadastro.html', {f'error_{d}': f'Campo {d} obrigatório!', 'pagina_atual': link})
        
        
        resultado = validarCadastroModel(request, nome, cpf, endereco, telefone, username, email, senha)

        if resultado == 'Sucesso':
            return render(request, 'cadastro.html', {'msg_success': 'Usuário cadastrado com sucesso!', 'pagina_atual': link})
        else:
            return render(request, 'cadastro.html', {'msg_error': 'Usuário indisponível', 'pagina_atual': link})

    
    else:
        return render(request, 'cadastro.html', {'pagina_atual': link})


def validarCadastroModel(request, nome, cpf, endereco, telefone, username, email, senha):
    userq = User.objects.filter(username=username).first()
    emailq = User.objects.filter(email=email).first()
    if userq or emailq:
        return 'Falha'
    else:
        user = User.objects.create_user(username=username, email=email, password=senha)
        usuario = Usuario.objects.create(nome=nome, cpf=cpf, endereco=endereco, telefone=telefone, usuario=user)
        usuario.save()
        user.save()        
        return 'Sucesso'


@login_required(login_url='/core/login')
def home(request):
    return render(request, 'home.html')

@login_required(login_url='/core/login')
def logout(request):
    logout_django(request)
    return redirect('../core/login')
    
    
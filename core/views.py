from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_django
from django.contrib.auth.decorators import login_required
from core.models import Usuario
from time import sleep

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        if len(username) == 0:
            return render(request, 'login.html', {'error_username': 'Campo usuário vazio!'})
        if len(senha) == 0:
            return render(request, 'login.html', {'error_senha': 'Campo senha vazio!'})
        
        return validarLoginModel(request, username, senha)
    
    else:
        return render(request, 'login.html')


def cadastro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        endereco = request.POST.get('endereco')
        telefone = request.POST.get('telefone')
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        resultado = validarCadastroModel(request, nome, cpf, endereco, telefone, username, email, senha)
        if resultado == 'Sucesso':
            return render(request, 'cadastro.html', {'msg_cadastro': 'Usuário cadastrado com sucesso!'})
        else:
            return render(request, 'cadastro.html', {'msg_cadastro': 'Usuário indisponível!'})
    else:
        return render(request, 'cadastro.html')
    

def validarLoginModel(request, username, senha):
    user =authenticate(username=username, password=senha)
    if user:
        login_django(request, user)
        return HttpResponse('Sucesso')
    else:
        return render(request, 'login.html', {'error_banco': 'Usuário ou senha inválidos!'})


def validarCadastroModel(request, nome, cpf, endereco, telefone, username, email, senha):
    user = User.objects.filter(username=username).first()
    if user:
        return 'Falha'
    user = User.objects.create_user(username=username, email=email, password=senha)
    usuario = Usuario.objects.create(nome=nome, cpf=cpf, endereco=endereco, telefone=telefone, usuario=user)
    usuario.save()
    user.save()        
    return 'Sucesso'


@login_required(login_url='/')
def home(request):
    return render(request, 'home.html')
    
    
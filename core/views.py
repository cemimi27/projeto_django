from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_django, logout as logout_django
from django.contrib.auth.decorators import login_required
from core.models import Usuario
from core import validator


def login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        validator.validarLogin(username, senha)
        context = validator.validarLogin(username, senha)
        if context:
            return render(request, 'login.html', context=context)
        else:
            return validarLoginModel(request, username, senha)
        
    else:
        return render(request, 'login.html')

def validarLoginModel(request, username, senha):
    user = authenticate(username=username, password=senha)
    if user:
        login_django(request, user)
        return redirect('../home')
    else:
        return render(request, 'login.html', {'erro_banco': 'Usuário ou senha inválidos!'})


def cadastro(request):

    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        endereco = request.POST.get('endereco')
        telefone = request.POST.get('telefone')
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        context = validator.validarCadastro(nome, cpf, endereco, telefone, username, email, senha)
        if context:
            return render(request, 'cadastro.html', context=context)
        else:        
            return validarCadastroModel(request, nome, cpf, endereco, telefone, username, email, senha)
    
    else:
        return render(request, 'cadastro.html')


def validarCadastroModel(request, nome, cpf, endereco, telefone, username, email, senha):
    context = dict()
    userq = User.objects.filter(username=username).first()
    emailq = User.objects.filter(email=email).first()
    if userq or emailq:
        context['erro_banco'] = 'Usuário indisponível!'
        return render(request, 'cadastro.html', context=context)
    else:
        context['sucesso'] = 'Usuário cadastrado com sucesso!'
        user = User.objects.create_user(username=username, email=email, password=senha)
        usuario = Usuario.objects.create(nome=nome, cpf=cpf, endereco=endereco, telefone=telefone, usuario=user)
        usuario.save()
        user.save()        
        return render(request, 'cadastro.html', context=context)


@login_required(login_url='/core/login')
def home(request):
    context = validator.dataAtual()
    return render(request, 'home.html', context=context)

@login_required(login_url='/core/login')
def logout(request):
    logout_django(request)
    return redirect('../core/login')
    
    
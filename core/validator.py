from django.core.exceptions import ValidationError, NON_FIELD_ERRORS
from django.contrib.auth.models import User

def validar_campo_vazio(value):
    if len(value) == 0:
        raise ValidationError(f'Campo {value} é obrgatório!', params={'value': value})


def validate_even(value):
    if not isinstance(value, int):
        raise ValueError('validate_even deve receber apenas números inteiros')

    if not value % 2 == 0:
        raise ValidationError(f'O número {value} não é par', params={'value': value})


def validar_usuario(value):
    if value is None:
        raise ValueError(f'O campo usuário é obrigatório!')

    userq = User.objects.filter(username=value).first()
    if userq:
        raise ValidationError(f'Usuário indisponível!', params={'value': value})

'''if len(nome) == 0:
            return render(request, 'cadastro.html', {'error_nome': 'Campo nome obrigatório!', 'pagina_atual': link})
        if len(cpf) == 0:
            return render(request, 'cadastro.html', {'error_cpf': 'Campo CPF obrigatório!', 'pagina_atual': link})
        if len(endereco) == 0:
            return render(request, 'cadastro.html', {'error_endereco': 'Campo endereço obrigatório!', 'pagina_atual': link})
        if len(telefone) == 0:
            return render(request, 'cadastro.html', {'error_telefone': 'Campo telefone obrigatório!', 'pagina_atual': link})
        if len(username) == 0:
            return render(request, 'cadastro.html', {'error_username': 'Campo usuário obrigatório!', 'pagina_atual': link})
        if len(email) == 0:
            return render(request, 'cadastro.html', {'error_email': 'Campo email obrigatório!', 'pagina_atual': link})
        if len(senha) == 0:
            return render(request, 'cadastro.html', {'error_senha': 'Campo senha obrigatório!', 'pagina_atual': link})'''




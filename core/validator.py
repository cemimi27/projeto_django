from datetime import datetime

def validarLogin(username, senha):
    context = dict()
    if not username:
        context['erro_username'] = 'Campo usuário obrigatório!'
    if not senha:
        context['erro_senha'] = 'Campo senha obrigatório!'
    return context

def validarCadastro(nome, cpf, endereco, telefone, username, email, senha):
    context = dict()
    if not nome:
        context['erro_nome'] = 'Campo nome obrigatório!'
    if not cpf:
        context['erro_cpf'] = 'Campo CPF obrigatório!'
    if not endereco:
        context['erro_endereco'] = 'Campo endereço obrigatório!'
    if not telefone:
        context['erro_telefone'] = 'Campo telefone obrigatório!'
    if not username:
        context['erro_username'] = 'Campo usuário obrigatório!'
    if not email:
        context['erro_email'] = 'Campo email obrigatório!'
    if not senha:
        context['erro_senha'] = 'Campo senha obrigatório!'
    return context

def dataAtual():
    context = dict()
    hora_atual = datetime.now().time().strftime('%H:%M')
    semana = ['Domingo', 'Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado']
    mes = ['Janeiro', 'Feveireiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto',
            'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    dia = datetime.now().date().day
    nmes = datetime.now().date().month
    ano = datetime.now().date().year
    dsemana = datetime.now().date().strftime('%w')
    s = int(dsemana)
    for i in range(0, 7):
        if i == s:
            dsemana = semana[i]
    m = int(nmes)
    for i in range(1, 13):
        if i == m:
            nmes = mes[i-1]
    context['data_atual'] = f'{dsemana}, {dia} de {nmes} de {ano}'
    context['hora_atual'] = hora_atual
    return context



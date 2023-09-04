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



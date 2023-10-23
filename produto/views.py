from django.shortcuts import render, HttpResponse
from .forms import FormularioProduto
from .models import Produto
from django.db.models.functions import Lower

def produtos(request):
    produtos = Produto.objects.order_by(Lower("nome_produto"))
    context = {'produtos': produtos}
    return render(request, 'produtos.html', context=context)

def detalhesProduto(request, cod_barras):
    produto = Produto.objects.get(cod_barras=cod_barras)
    context = {'produto': produto}

    return render(request, 'produtodetalhe.html', context=context)

def cadastroProduto(request):
    formulario = FormularioProduto
    context = {'formulario': formulario, 'msg': ''}
    if request.method == 'POST':
        nome_produto = request.POST.get('nome_produto')
        cod_barras = request.POST.get('cod_barras')
        preco_produto = request.POST.get('preco_produto')
        qtd_produto = request.POST.get('qtd_produto')
        descricao = request.POST.get('descricao')
        #context = {'Nome': nome_produto}
        #return render(request, 'cadastroproduto.html', context=context)
        msg = validarCadastroProdutoModel(request, nome_produto, cod_barras, preco_produto, qtd_produto, descricao)
        context['msg'] = msg
        return render(request, 'cadastroproduto.html', context=context)
    else:
        return render(request, 'cadastroproduto.html', context=context)

def validarCadastroProdutoModel(request, nome_produto, cod_barras, preco_produto, qtd_produto, descricao):
    msg = dict()
    produto = Produto.objects.filter(nome_produto=nome_produto)
    if produto:
        msg['msg'] = 'Produto já cadastrado no sistema!'
        return msg
    else:
        produto = Produto(nome_produto=nome_produto, cod_barras=cod_barras, preco_produto=preco_produto,
                           qtd_produto=qtd_produto, descricao=descricao)
        produto.save()
        msg['msg'] = 'Produto cadastrado com sucesso!'
        return msg


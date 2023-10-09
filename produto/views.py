from django.shortcuts import render, HttpResponse
from .forms import FormularioProduto
from .models import Produto

def produtos(request):
    produtos = Produto.objects.all()
    context = {'produtos': produtos}
    return render(request, 'produtos.html', context=context)

def cadastroProduto(request):
    if request.method == 'POST':
        nome_produto = request.POST.get('nome_produto')
        cod_barras = request.POST.get('cod_barras')
        preco_produto = request.POST.get('preco_produto')
        qtd_produto = request.POST.get('qtd_produto')
        descricao = request.POST.get('descricao')
        #context = {'Nome': nome_produto}
        #return render(request, 'cadastroproduto.html', context=context)
        return validarCadastroProdutoModel(request, nome_produto, cod_barras, preco_produto, qtd_produto, descricao)
    else:
        formulario = FormularioProduto
        context = {'formulario': formulario}
        return render(request, 'cadastroproduto.html', context=context)

def validarCadastroProdutoModel(request, nome_produto, cod_barras, preco_produto, qtd_produto, descricao):
    produto = Produto.objects.filter(nome_produto=nome_produto)
    if produto:
        return HttpResponse('Achei')
    else:
        return HttpResponse('Não achei')


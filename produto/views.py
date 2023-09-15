from django.shortcuts import render, HttpResponse
from .forms import FormularioProduto

# Create your views here.
def cadastroProduto(request):
    formulario = FormularioProduto
    context = {'formulario': formulario}
    return render(request, 'cadastroproduto.html', context=context)

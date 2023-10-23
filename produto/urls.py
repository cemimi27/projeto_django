from django.urls import path
from . import views

app_name = 'produto'

urlpatterns = [
    path('produtos/', views.produtos, name='produtos'),
    path('detalhes/<int:cod_barras>/', views.detalhesProduto, name='detalhes'),
    path('cadastro/', views.cadastroProduto, name='cadastro'),
]
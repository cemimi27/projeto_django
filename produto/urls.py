from django.urls import path
from . import views

app_name = 'produto'

urlpatterns = [
    path('produtos/', views.produtos, name='produtos'),
    path('cadastro/', views.cadastroProduto, name='cadastro'),
]
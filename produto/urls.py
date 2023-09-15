from django.urls import path
from . import views

app_name = 'produto'

urlpatterns = [
    path('cadastro/', views.cadastroProduto, name='cadastro')
]
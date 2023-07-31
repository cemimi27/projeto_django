from django.urls import path
from core import views

app_name = 'core'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('home/', views.home, name='home')
    #path('validarLogin/', views.validarLogin, name="validarLogin"),
]
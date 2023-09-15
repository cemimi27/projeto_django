from django.db import models
from django.contrib.auth.models import User

LIST_TIPO = [
    ('Administrador', 'ADM'),
    ('Cliente', 'CLI'),
    ('Funcionário', 'FUN')
]

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=255, null=False)
    cpf = models.CharField(max_length=14, null=True)
    endereco = models.CharField(max_length=255, null=True)
    telefone = models.CharField(max_length=16, null=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50, choices=LIST_TIPO, default='Cliente')
    def __str__(self):
        return str(self.nome)

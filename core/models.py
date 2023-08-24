from django.db import models
from django.contrib.auth.models import User
from .validator import validar_campo_vazio, validate_even, validar_usuario


# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=255, null=False)
    cpf = models.CharField(max_length=14, null=True)
    endereco = models.CharField(max_length=255, null=True)
    telefone = models.CharField(max_length=16, null=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nome)

class Teste(models.Model):
    campo1 = models.IntegerField(validators=[validate_even])

    def __str__(self):
        return str(self.campo1)

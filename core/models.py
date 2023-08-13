from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from core.validators import clean

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=255, null=False, validators=[clean], default='')
    cpf = models.CharField(max_length=14, null=False)
    endereco = models.CharField(max_length=255, null=False, default='')
    telefone = models.CharField(max_length=16, null=False, default='')
    usuario = models.OneToOneField(User, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nome)

class Nome(models.Model):
    nome = models.CharField(max_length=255, validators=[clean])



    
    

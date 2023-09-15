from django.db import models

class Produto(models.Model):
    nome_produto = models.CharField(max_length=255)
    cod_barras = models.IntegerField(max_length=13)
    preco_produto = models.IntegerField(max_length=10)
    qtd_produto = models.IntegerField(max_length=10)
    descricao = models.CharField(max_length=255)

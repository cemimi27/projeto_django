from django.db import models

class Produto(models.Model):
    nome_produto = models.CharField(max_length=255)
    cod_barras = models.IntegerField()
    preco_produto = models.IntegerField()
    qtd_produto = models.IntegerField()
    descricao = models.TextField(max_length=255)

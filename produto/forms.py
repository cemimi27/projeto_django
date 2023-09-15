from django import forms
from .models import Produto

class FormularioProduto(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome_produto', 'cod_barras', 'preco_produto',
                  'qtd_produto', 'descricao']
        labels = {'nome_produto': 'Nome', 'cod_barras': 'Código de Barras', 'preco_produto': 'Preço',
                  'qtd_produto': 'Quantidade', 'descricao': 'Descrição'}
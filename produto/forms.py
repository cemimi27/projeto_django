from django import forms
from .models import Produto

class FormularioProduto(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome_produto', 'cod_barras', 'preco_produto',
                  'qtd_produto', 'descricao']
        
        labels = {'nome_produto': 'Nome', 'cod_barras': 'Código de Barras', 'preco_produto': 'Preço',
                  'qtd_produto': 'Quantidade', 'descricao': 'Descrição'}

        widgets = {'nome_produto': forms.TextInput(attrs={'class': 'form-control opacity-75 col-9','placeholder': 'Informe o nome do produto'}),
                    'cod_barras': forms.TextInput(attrs={'class': 'form-control opacity-75 col-9', 'placeholder': 'Informe o código de barras'}),
                      'preco_produto': forms.TextInput(attrs={'class': 'form-control opacity-75 col-9', 'placeholder': 'Informe o valor'}),
                        'qtd_produto': forms.TextInput(attrs={'class': 'form-control opacity-75 col-9', 'placeholder': 'Informe a quantidade'}),
                          'descricao': forms.Textarea(attrs={'class': 'form-control opacity-75 col-9', 'placeholder': 'Informe uma descrição', 'rows': '5'})
                  }
        
        
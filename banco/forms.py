from django import forms
from .models import Cliente
from .models import Cartao
from .models import Emprestimo

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'cpf']

class CartaoForm(forms.ModelForm):
    class Meta:
        model = Cartao
        fields = ['empresa_responsavel', 'cliente', 'limite', 'fatura']

class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['cliente', 'valorEmprestimo', 'prazo']
from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.nome+ ' - ' +self.cpf
    
class Cartao(models.Model):
    empresa_responsavel = models.TextField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    limite = models.CharField(max_length=15)
    fatura = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self): 
        return f"{self.cliente} - {self.limite} - {self.fatura}"
    
class Emprestimo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    valorEmprestimo = models.CharField(max_length=15)
    prazo = models.DateField()

    def __str__(self): 
        return f"{self.cliente} - {self.valorEmprestimo} - {self.prazo}"
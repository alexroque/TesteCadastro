import email
from pyexpat import model
from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=200, unique=True)
    data_cadastro = models.DateField()
    data_atualizacao = models.DateField()
    
    def __str__(self):
        return self.nome

class Fornecedor(models.Model):
    nome_fantasia = models.CharField(max_length=300)
    razao_social = models.CharField(max_length=300)
    endereco = models.CharField(max_length=300)
    cnpj = models.CharField(max_length=18)
    telefones = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nome_fantasia
    
class Produto(models.Model):
    nome = models.CharField(max_length=200, unique=True)
    data_cadastro = models.DateField
    data_atualizacao = models.DateField
    descricao = models.CharField(max_length=400)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="produtos")

    def __str__(self):
        return "%s (%s)" %(self.nome, self.descricao)

class Itens_Produto(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name="produto")
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.PROTECT, related_name="fornecedor")
    custo = models.FloatField()

    def __str__(self):
        return "%s (%s) (%s)" %(self.produto.nome, self.fornecedor.nome_fantasia, self.custo)


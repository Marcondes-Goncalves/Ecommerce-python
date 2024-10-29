from pickle import FALSE
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# os ids são criados automáticamente

class Cliente(models.Model):
    # Os parâmetros null e blank estão True, pois isso possibilita que o usuário realize uma compra sem criar uma conta nesse modelo de negocio
    nome = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    telefone = models.CharField(max_length=200, null=True, blank=True)
    id_sessao = models.CharField(max_length=200, null=True, blank=True)
    # cada USUÁRIO só poderá ter um cliente e vice-versa
    # on_delete=models.CASCADE - se o usuário for deletado os dados ligados a ele também serão deletados
    usuario = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE) # um para um


class Categoria(models.Model):
    nome = models.CharField(max_length=200, null=True, blank=True)


class Tipo(models.Model):
    nome = models.CharField(max_length=200, null=True, blank=True)


class Produto(models.Model):
    # obs: nome da imagem
    imagem = models.CharField(max_length=400, null=True, blank=True)
    nome = models.CharField(max_length=200, null=True, blank=True)
    # preço de no máximo 10 digítos e com duas casas decimais. exemplo: 99.000.000,00
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    ativo = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, null=True, blank=True, on_delete=models.SET_NULL)
    tipo = models.ForeignKey(Tipo, null=True, blank=True, on_delete=models.SET_NULL)


class ItemEstoque(models.Model):
    produto = models.ForeignKey(Produto, null=True, blank=True, on_delete=models.SET_NULL)
    cor = models.CharField(max_length=200, null=True, blank=True)
    tamanho = models.CharField(max_length=200, null=True, blank=True)
    quantidade = models.IntegerField(default=0)


class Endereco(models.Model):
    rua = models.CharField(max_length=200, null=True, blank=True)
    número = models.IntegerField(default=0)
    complemento = models.CharField(max_length=200, null=True, blank=True)
    cep = models.CharField(max_length=200, null=True, blank=True)
    cidade = models.CharField(max_length=200, null=True, blank=True)
    estado = models.CharField(max_length=200, null=True, blank=True)
    cliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.SET_NULL)


class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.SET_NULL)
    data_finalização = models.DateTimeField(null=True, blank=True)
    finalizado = models.BooleanField(default=False)
    codigo_transação = models.CharField(max_length=200, null=True, blank=True)
    endereço = models.ForeignKey(Endereco, null=True, blank=True, on_delete=models.SET_NULL)


class ItensPedido(models.Model):
    itemEstoque = models.ForeignKey(ItemEstoque, null=True, blank=True, on_delete=models.SET_NULL)
    quantidade = models.IntegerField(default=0)
    pedido = models.ForeignKey(Pedido, null=True, blank=True, on_delete=models.SET_NULL)




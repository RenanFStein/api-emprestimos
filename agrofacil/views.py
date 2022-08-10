from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import *
from .serializer import *

class EmpresaViewSet(viewsets.ModelViewSet):
    """ ViewSet Empresa """
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class ClientesViewSet(viewsets.ModelViewSet):
    """ ViewSet Clientes """
    queryset = Cliente.objects.all()
    serializer_class = ClientesSerializer

class FornecedorViewSet(viewsets.ModelViewSet):
    """ ViewSet Fornecedor """
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer

class CaixaViewSet(viewsets.ModelViewSet):
    """ ViewSet Fornecedor """
    queryset = Caixa.objects.all()
    serializer_class = CaixaSerializer

class VendasViewSet(viewsets.ModelViewSet):
    """ ViewSet Vendas """
    queryset = Vendas.objects.all()
    serializer_class = VendasSerializer     

class ComprasViewSet(viewsets.ModelViewSet):
    """ ViewSet Compras """
    queryset = Compras.objects.all()
    serializer_class = ComprasSerializer       

class ProdutosViewSet(viewsets.ModelViewSet):
    """ ViewSet Vendas """
    queryset = Produto.objects.all()
    serializer_class = ProdutosSerializer  

class EstoquesViewSet(viewsets.ModelViewSet):
    """ ViewSet Estoques """
    queryset = Estoque.objects.all()
    serializer_class = EstoquesSerializer  
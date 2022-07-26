from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import *
from .serializer import *

class ClienteViewSet(viewsets.ModelViewSet):
    """ ViewSet Dados do Cliente """
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer        

class BancoClienteViewSet(viewsets.ModelViewSet):
    """ ViewSet Cliente """
    queryset = BancoCliente.objects.all()
    serializer_class = BancoClienteSerializer

class TabelaTaxasViewSet(viewsets.ModelViewSet):
    """ ViewSet Tabela de Juros """
    queryset = TabelaTaxas.objects.all()
    serializer_class = TabelaTaxasSerializer        

class ParcelasViewSet(viewsets.ModelViewSet):
    """ ViewSet Tabelas de Juros """
    queryset = Parcelas.objects.all()
    serializer_class = ParcelasSerializer

class SolicitacaoViewSet(viewsets.ModelViewSet):
    """ ViewSet Solicitações """
    queryset = Solicitacao.objects.all()
    serializer_class = SolicitacaoSerializer
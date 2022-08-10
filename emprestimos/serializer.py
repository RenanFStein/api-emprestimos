from django.forms import ValidationError
from rest_framework.views import exception_handler
from rest_framework import serializers
from .models import *



class ClienteSerializer(serializers.ModelSerializer):
    """ Serialização do model Cliente """
    class Meta:
        model = Cliente
        fields = ['id', 'cliente', 'telefone_cliente', 'cpf_cliente']

class BancoClienteSerializer(serializers.ModelSerializer):
    """ Serialização do model Banco """
    cliente_banco = ClienteSerializer()
    class Meta:
        model = BancoCliente
        fields = ['nome_banco', 'tipo_conta', 'numero_conta', 'cliente_banco']


    def create(self, validated_data):
        profile_data = validated_data.pop('cliente_banco')
        print(profile_data)
        user=Cliente.objects.create(cliente= profile_data['cliente'], 
                                    telefone_cliente  =  profile_data['telefone_cliente'], 
                                    cpf_cliente  = profile_data['cpf_cliente'])
                                    
        return BancoCliente.objects.create(cliente_banco=user, **validated_data)

class TabelaTaxasSerializer(serializers.ModelSerializer):
    """ Serialização do model Tabela de Taxas """
    class Meta:
        model = TabelaTaxas
        fields = ['id','nome_tabela']

class ParcelasSerializer(serializers.ModelSerializer):
    """ Serialização do model Parcelas """
    tabela = TabelaTaxasSerializer()
    class Meta:
        model = Parcelas
        fields = [  'tabela', 'id', 'parcela', 'juros_parcela', 'valor_parcela', 'valor_total', 'comissao']


    def create(self, validated_data):
        profile_data = validated_data.pop('tabela')
        print(profile_data['nome_tabela'])
        print(validated_data['parcela'])
        tabela=TabelaTaxas.objects.create(nome_tabela= profile_data['nome_tabela'])
        return Parcelas.objects.create(tabela= tabela, **validated_data)

class SolicitacaoSerializer(serializers.ModelSerializer):
    """ Serialização do model Solicitações """
    class Meta:
        model = Solicitacao
        fields = ['id_cliente_banco', 
                  'juros_parcela', 
                  'valor_juros_parcelado', 
                  'comissao', 
                  'valor_comissao', 
                  'valor_parcela', 
                  'numero_cartao', 
                  'valor_desejado', 
                  'total_emprestimo', 
                  'id_parcela', 
                  'id_tabela_taxas']
    
    def validate_valor_desejado(self, valor_desejado):
        if valor_desejado < 300:             
            raise serializers.ValidationError('Valor Minimo para solicitação é de R$ 300,00')
        if valor_desejado > 10000:             
            raise serializers.ValidationError('Valor Maximo para solicitação é de R$ 10.000,00')
        return valor_desejado
            
          
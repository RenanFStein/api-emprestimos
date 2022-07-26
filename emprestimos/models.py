import re
from tabnanny import verbose
from django.db import models

class TabelaTaxas(models.Model):
    nome_tabela = models.CharField(verbose_name="Tabela de Juros", max_length=255, blank=False, null=False)

    def __str__(self):
        tabela = f'Nº {str(self.id)}'
        return tabela
    
    class Meta:
        verbose_name = "Tabela de Juros"
        verbose_name_plural = "Tabela de Juros"

class Parcelas(models.Model):
    tabela = models.ForeignKey(TabelaTaxas, verbose_name="Tabela de Juros", on_delete=models.CASCADE, null=True, blank=True)
    parcela = models.DecimalField(verbose_name="Parcela", max_digits=19, decimal_places=2)
    juros_parcela = models.DecimalField(verbose_name="Juros da Parcela", max_digits=19, decimal_places=2)
    valor_parcela = models.DecimalField(verbose_name="Valor da Parcela", max_digits=19, decimal_places=2)
    valor_total = models.DecimalField(verbose_name="Valor Total", max_digits=19, decimal_places=2)
    comissao = models.DecimalField(verbose_name="Comissão", max_digits=19, decimal_places=2)

    def __str__(self):
        return "Parcelas"

    class Meta:
        verbose_name = "Parcelas"
        verbose_name_plural = "Parcelas"

class Cliente(models.Model):
    cliente = models.CharField(verbose_name="Cliente", max_length=255, blank=False, null=False)
    telefone_cliente = models.CharField(verbose_name="Telefone", max_length=15, blank=False, null=False)
    cpf_cliente = models.CharField(verbose_name="CPF", max_length=11, blank=False, null=False)   

    def __str__(self):
        return self.cliente
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Cliente"

class BancoCliente(models.Model):
    cliente_banco = models.ForeignKey(Cliente, verbose_name="Cliente", on_delete=models.CASCADE, null=True, blank=True)
    nome_banco = models.CharField(verbose_name="Nome do Banco", max_length=11, blank=False, null=False)
    tipo_conta = models.CharField(verbose_name="Tipo da Conta", max_length=11, blank=False, null=False)
    numero_conta = models.CharField(verbose_name="Numero da Conta", max_length=11, blank=False, null=False)   
    
    def __str__(self):
        return self.nome_banco
    class Meta:
        verbose_name = "Banco"
        verbose_name_plural = "Banco"

class Solicitacao(models.Model):
    
    id_cliente_banco = models.ForeignKey(Cliente, verbose_name="ID Cliente", on_delete=models.CASCADE, null=True, blank=True)
    juros_parcela = models.DecimalField(verbose_name="Juros Parcela", max_digits=19, decimal_places=2)
    valor_juros_parcelado = models.DecimalField(verbose_name="Valor do Juros Parcelado", max_digits=19, decimal_places=2)
    comissao = models.DecimalField(verbose_name="Comissão", max_digits=19, decimal_places=2)
    valor_comissao = models.DecimalField(verbose_name="Valor da Comissão", max_digits=19, decimal_places=2)
    valor_parcela = models.DecimalField(verbose_name="Valor da Parcela", max_digits=19, decimal_places=2)
    numero_cartao = models.DecimalField(verbose_name="Numero Cartão", max_digits=30, decimal_places=0)
    valor_desejado = models.DecimalField(verbose_name="Valor Desejado", max_digits=19, decimal_places=2)
    total_emprestimo = models.DecimalField(verbose_name="Total Emprestimo", max_digits=19, decimal_places=2)
    id_parcela = models.ForeignKey(Parcelas, verbose_name="ID  Parcela", on_delete=models.CASCADE, null=True, blank=True)
    id_tabela_taxas = models.ForeignKey(TabelaTaxas, verbose_name="ID Tabela de Taxas", on_delete=models.CASCADE, null=True, blank=True)
    
   
    def __str__(self):
        solicitacao = f'Nº {str(self.id)}'
        return solicitacao
    
    class Meta:
        verbose_name = "Solicitações"
        verbose_name_plural = "Solicitações"    


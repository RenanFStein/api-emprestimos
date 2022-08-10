from re import T
from tabnanny import verbose
from django.db import models
from .models import *
from django.db.models import Sum, Min, Max, Count, Avg


class Empresa(models.Model):
    nome_empresa = models.CharField(verbose_name="Nome da Empresa", max_length=255, blank=False, null=False)
    cnpj_empresa = models.CharField(verbose_name="Empresa CNPJ", max_length=14,unique=True, blank=False, null=False)
    cep_empresa =  models.CharField(verbose_name="CEP da Empresa", max_length=8, blank=False, null=False)
    endereco_empresa = models.CharField(verbose_name="Endereço da Empresa", max_length=255, blank=False, null=False)
    numero_endereco_empresa = models.CharField(verbose_name="Numero do Endereço", max_length=8, blank=False, null=False)
    complemento_endereco_empresa = models.CharField(verbose_name="Complemento do Endereço",max_length=255, blank=True, null=True)
    telefone_empresa = models.CharField(verbose_name="Telefone da Empresa", max_length=14, blank=False, null=False)
    email_empresa = models.CharField(verbose_name="Email da Empresa", max_length=255, blank=False, null=False)
    cidade_empresa = models.CharField(verbose_name="Cidade da Empresa", max_length=255, blank=False, null=False)
    uf_empresa = models.CharField(verbose_name="UF da Empresa", max_length=2, blank=False, null=False)
    def __str__(self):
        dados = f'Empresa: {str(self.nome_empresa)}'
        return dados
    
    class Meta:
        verbose_name = "Cadastro Empresa"
        verbose_name_plural = "Cadastro Empresa"

class Fornecedor(models.Model):
    nome_fornecedor = models.CharField(verbose_name="Nome da Fornecedor", max_length=255, blank=False, null=False)
    cnpj_fornecedor = models.CharField(verbose_name="Fornecedor CNPJ", max_length=14,unique=True, blank=False, null=False)
    telefone_fornecedor = models.CharField(verbose_name="Telefone da Fornecedor", max_length=14, blank=False, null=False)
    email_fornecedor = models.CharField(verbose_name="Email da Fornecedor", max_length=255, blank=False, null=False)
    endereco_fornecedor = models.CharField(verbose_name="Endereço do Fornecedor", max_length=255, blank=False, null=False)
    numero_endereco_fornecedor = models.CharField(verbose_name="Numero do Fornecedor", max_length=8, blank=False, null=False)
    cep_fornecedor =  models.CharField(verbose_name="CEP da Fornecedor", max_length=8, blank=False, null=False) 
    complemento_endereco_fornecedor = models.CharField(verbose_name="Complemento do Endereço",max_length=255, blank=True, null=True)
    cidade_fornecedor = models.CharField(verbose_name="Cidade da Fornecedor", max_length=255, blank=False, null=False)
    uf_fornecedor = models.CharField(verbose_name="UF da Fornecedor", max_length=2, blank=False, null=False)
    def __str__(self):
        dados = f'Fornecedor: {str(self.nome_fornecedor)}'
        return dados
    
    class Meta:
        verbose_name = "Cadastro Fornecedor"
        verbose_name_plural = "Cadastro Fornecedor"

class Cliente(models.Model):
    nome_cliente = models.CharField(verbose_name="Nome da Cliente", max_length=255, blank=False, null=False)
    cnpj_cliente = models.CharField(verbose_name="Cliente CNPJ", max_length=14,unique=True, blank=False, null=False)
    telefone_cliente = models.CharField(verbose_name="Telefone da Cliente", max_length=14, blank=False, null=False)
    email_cliente = models.CharField(verbose_name="Email da Cliente", max_length=255, blank=False, null=False)
    endereco_cliente = models.CharField(verbose_name="Endereço do Cliente", max_length=255, blank=False, null=False)
    numero_endereco_cliente = models.CharField(verbose_name="Numero do Cliente", max_length=8, blank=False, null=False)
    cep_cliente =  models.CharField(verbose_name="CEP da Cliente", max_length=8, blank=False, null=False) 
    complemento_endereco_cliente = models.CharField(verbose_name="Complemento do Endereço", max_length=255, blank=True, null=True)
    cidade_cliente = models.CharField(verbose_name="Cidade da Cliente", max_length=255, blank=False, null=False)
    uf_cliente = models.CharField(verbose_name="UF da Cliente", max_length=2, blank=False, null=False)
    def __str__(self):
        dados = f'Cliente: {str(self.nome_cliente)}'
        return dados
    
    class Meta:
        verbose_name = "Cadastro Cliente"
        verbose_name_plural = "Cadastro Cliente"


class Produto(models.Model):
    nomeProduto = models.CharField(verbose_name="Nome do Produto", max_length=255, blank=False, null=False)
    descricao_produto = models.CharField(verbose_name="Descrição do Produto", max_length=255, blank=False, null=False)
    
    def quantidade_estoque(self):
        if Estoque.objects.filter(produto=self.id).values_list('produto'):
            dados = Estoque.objects.filter(produto=self.id).values_list('produto').annotate(Sum('quantidade'))
            dados = str(dados[0][1])
            return dados
 

    def custo_medio(self):   
        if Estoque.objects.filter(produto=self.id).values_list('produto'):         
            dados = Estoque.objects.filter(produto=self.id).values_list('produto').annotate(Avg('valor'))
            dados = float(dados[0][1])
            return dados 

    def valor_estoque(self):    
        if Estoque.objects.filter(produto=self.id).values_list('produto'):        
            quantidade_estoque = Estoque.objects.filter(produto=self.id).values_list('produto').annotate(Avg('valor'))
            custo_medio = Estoque.objects.filter(produto=self.id).values_list('produto').annotate(Sum('quantidade'))
            dados = float(f'{(float(quantidade_estoque[0][1]) * float(custo_medio[0][1])):.4f}')  
            return dados   
 
    def __str__(self):
        dados = f'Produto: {str(self.nomeProduto)}'   
        return dados    

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
    
class Estoque(models.Model):  
    produto = models.ForeignKey(Produto, verbose_name="Produtos", null=False, blank=False, on_delete=models.CASCADE)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)  
    valor = models.DecimalField(max_digits=10, decimal_places=2)    

    
    def descricao_produto(self):            
        estoq = Produto.objects.filter(id=self.produto.id).values_list().annotate(Sum('id'))
        return estoq[0][2]


    def __str__(self):
        dados = f'Produto:'   
        return dados
    
    
    class Meta:
        verbose_name = "Estoque"
        verbose_name_plural = "Estoque"

class Compras(models.Model):
    fornecedor = models.ForeignKey(Fornecedor, verbose_name="Fornecedores", null=False, blank=False, on_delete=models.CASCADE)
    estoque = models.ForeignKey(Estoque, verbose_name="Estoque", null=False, blank=False, on_delete=models.CASCADE) 

    def __str__(self):
        dados = f'Compra nº{str(self.id)} do fornecedor {str(self.fornecedor.nome_fornecedor)}'
        return dados

    def produto(self):            
        estoq = Compras.objects.filter(estoque=self.estoque).values_list()
        produto = Estoque.objects.filter(id=estoq[0][2]).values_list()
        prod = Produto.objects.filter(id=produto[0][1]).values_list()
        return prod[0][1]

    def quantidade(self):            
        estoq = Compras.objects.filter(estoque=self.estoque).values_list()
        quantidade_produto = Estoque.objects.filter(id=estoq[0][2]).values_list()
  
        return quantidade_produto[0][2]

    def valor(self):            
        estoq = Compras.objects.filter(estoque=self.estoque).values_list()
        valor_produto = Estoque.objects.filter(id=estoq[0][2]).values_list()
     
        return valor_produto[0][3]
    
    def total_compra(self):            
        quantidade  =  self.quantidade() * self.valor()
        return quantidade
    
    class Meta:
        verbose_name = "Compra"
        verbose_name_plural = "Compras"

class Vendas(models.Model):

    cliente = models.ForeignKey(Cliente, verbose_name="Clientes", null=False, blank=False, on_delete=models.CASCADE)
    estoque = models.ForeignKey(Estoque, verbose_name="Estoque", null=False, blank=False, on_delete=models.CASCADE) 

    def __str__(self):
        dados = f'Venda nº{str(self.id)} para o Cliente {str(self.cliente.nome_cliente)}'
        return dados

    def produto(self):            
        estoq = Vendas.objects.filter(estoque=self.estoque).values_list()
        produto = Estoque.objects.filter(id=estoq[0][2]).values_list()
        prod = Produto.objects.filter(id=produto[0][1]).values_list()
        return prod[0][1]

    def quantidade(self):            
        estoq = Vendas.objects.filter(estoque=self.estoque).values_list()
        quantidade_produto = Estoque.objects.filter(id=estoq[0][2]).values_list()
  
        return quantidade_produto[0][2]

    def valor(self):            
        estoq = Vendas.objects.filter(estoque=self.estoque).values_list()
        valor_produto = Estoque.objects.filter(id=estoq[0][2]).values_list()
     
        return valor_produto[0][3]
    
    def total_venda(self):            
        quantidade  =  self.quantidade() * self.valor()
        return quantidade

    class Meta:
        verbose_name = "Venda"
        verbose_name_plural = "Vendas"

class Caixa(models.Model):
         
    vendas = models.ForeignKey(Vendas, verbose_name="Venda", null=True, blank=True, on_delete=models.CASCADE)
    compras = models.ForeignKey(Compras, verbose_name="Compra", null=True, blank=True, on_delete=models.CASCADE)  
    status = models.BooleanField(verbose_name="Pago ?" )  

    def __str__(self):
        dados = f'Caixa'
        return dados
    
    class Meta:
        verbose_name = "Caixa"
        verbose_name_plural = "Caixa"

from dataclasses import field
from django.contrib import admin
from .models import *
from django.db.models import Sum


class EmpresaAdmin(admin.ModelAdmin):
    list_display= ('id','nome_empresa','cnpj_empresa', 'email_empresa','cidade_empresa','uf_empresa')
    list_display_links= ('nome_empresa',)
    list_filter = ('nome_empresa',) 
admin.site.register(Empresa, EmpresaAdmin)

class FornecedorAdmin(admin.ModelAdmin):
    list_display= ('id','nome_fornecedor','cnpj_fornecedor', 'email_fornecedor','cidade_fornecedor','uf_fornecedor')
    list_display_links= ('nome_fornecedor',)
    list_filter = ('nome_fornecedor',) 
admin.site.register(Fornecedor, FornecedorAdmin)

class ClienteAdmin(admin.ModelAdmin):
    list_display= ('id','nome_cliente','cnpj_cliente', 'email_cliente','cidade_cliente','uf_cliente')
    list_display_links= ('nome_cliente',)
    list_filter = ('nome_cliente',) 
admin.site.register(Cliente, ClienteAdmin)

class VendasAdmin(admin.ModelAdmin):
    list_display= ('id','cliente', 'produto','quantidade','valor', 'total_venda')
    list_display_links= ('cliente',)
    list_filter = ('cliente',) 
admin.site.register(Vendas, VendasAdmin)

class ComprasAdmin(admin.ModelAdmin):
    list_display= ('id','fornecedor', 'produto','quantidade','valor', 'total_compra')
    list_display_links= ('fornecedor',)
    list_filter = ('fornecedor',)     
admin.site.register(Compras, ComprasAdmin) 



class EstoqueAdmin(admin.ModelAdmin):
    list_display= ('id','produto','quantidade', 'valor','descricao_produto')
    list_filter = ('produto',) 

admin.site.register(Estoque, EstoqueAdmin)

class EstoqueInline(admin.TabularInline):
    model = Estoque
    extra = 1
    

class ProdutoAdmin(admin.ModelAdmin):
    inlines = [
        EstoqueInline,
        
    ]    
    list_display= ('nomeProduto','descricao_produto','quantidade_estoque', 'custo_medio', 'valor_estoque')
    list_filter = ('nomeProduto',)
    search_fields = ('nomeProduto',)    
admin.site.register(Produto, ProdutoAdmin) 

class CaixaAdmin(admin.ModelAdmin):
    
    list_display= ('id','vendas','compras','status', )
    list_display_links= ('vendas','compras', )
    list_filter = ('vendas','compras','status', )
    search_fields = ('vendas','compras',)    
admin.site.register(Caixa, CaixaAdmin) 


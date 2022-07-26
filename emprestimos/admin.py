from django.contrib import admin
from .models import *


class ParcelasInline(admin.TabularInline):
    model = Parcelas
    extra = 1


class TabelaTaxasAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_tabela')    
    inlines = [
        ParcelasInline,
    ]  
admin.site.register(TabelaTaxas, TabelaTaxasAdmin)


class BancoClienteInline(admin.TabularInline):
    model = BancoCliente
    extra = 1
class ClienteAdmin(admin.ModelAdmin):
    inlines = [
        BancoClienteInline,
    ]
admin.site.register(Cliente, ClienteAdmin)
   
admin.site.register(BancoCliente)


class SolicitacaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'juros_parcela')
admin.site.register(Solicitacao, SolicitacaoAdmin)
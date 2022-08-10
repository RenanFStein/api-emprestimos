from django.urls import path, include
from rest_framework import routers
from .views import *
from .serializer import *

router = routers.DefaultRouter()

router.register('Empresa',EmpresaViewSet, basename='Empresa')

router.register('Clientes',ClientesViewSet, basename='Clientes')
router.register('Fornecedor',FornecedorViewSet, basename='Fornecedor')


router.register('Produtos',ProdutosViewSet, basename='Produtos')
router.register('Estoques',EstoquesViewSet, basename='Estoques')
router.register('Compras', ComprasViewSet, basename='Compras')
router.register('Vendas',VendasViewSet, basename='Vendas')

router.register('Caixa', CaixaViewSet, basename='Caixa')

urlpatterns = [
    path('api/', include(router.urls)),

]
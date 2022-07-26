from django.urls import path, include
from rest_framework import routers
from .views import *
from .serializer import *

router = routers.DefaultRouter()
router.register('BancoCliente', BancoClienteViewSet, basename='BancoCliente')
router.register('Parcelas', ParcelasViewSet, basename='Parcelas')
router.register('Solicitacoes', SolicitacaoViewSet, basename='Solicitacao')

urlpatterns = [
    path('api/', include(router.urls)),

]
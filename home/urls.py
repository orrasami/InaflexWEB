from django.urls import path, include

from .views import index, inspecao, recebimento, liberacao_pedidos, administracao

urlpatterns = [
    path('', index, name='home_index'),
    path('inspecao/', inspecao, name='home_inspecao'),
    path('recebimento/', recebimento, name='home_recebimento'),
    path('liberacao_pedidos/', liberacao_pedidos, name='home_liberacao_pedidos'),
    path('administracao/', administracao, name='home_administracao'),
]

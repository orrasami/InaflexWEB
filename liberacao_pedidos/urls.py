from django.urls import path

from .views import liberacao_pedidos_index, liberacao_pedidos_orcamento, liberacao_pedidos_editar, liberacao_pedidos_logout, liberacao_pedidos_salvar_orcamento, liberacao_pedidos_novo_orcamento

urlpatterns = [
    path('', liberacao_pedidos_index, name='liberacao_pedidos_index'),
    path('orcamento', liberacao_pedidos_orcamento, name='liberacao_pedidos_orcamento'),
    path('editar', liberacao_pedidos_editar, name='liberacao_pedidos_editar'),
    path('novo_orcamento', liberacao_pedidos_novo_orcamento, name='liberacao_pedidos_novo_orcamento'),
    path('salvar_orcamento', liberacao_pedidos_salvar_orcamento, name='liberacao_pedidos_salvar_orcamento'),
    path('logout', liberacao_pedidos_logout, name='liberacao_pedidos_logout'),
]

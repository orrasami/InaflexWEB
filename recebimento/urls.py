from django.urls import path

from .views import recebimento_index, recebimento_lote, recebimento_editar, recebimento_logout, recebimento_salvar_lote, recebimento_novo_lote

urlpatterns = [
    path('', recebimento_index, name='recebimento_index'),
    path('lote', recebimento_lote, name='recebimento_lote'),
    path('editar', recebimento_editar, name='recebimento_editar'),
    path('novo_lote', recebimento_novo_lote, name='recebimento_novo_lote'),
    path('salvar_lote', recebimento_salvar_lote, name='recebimento_salvar_lote'),
    path('logout', recebimento_logout, name='recebimento_logout'),
]

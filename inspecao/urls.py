from django.urls import path

from .views import inspecao_index, inspecao_lote, inspecao_finalizar, inspecao_editar, inspecao_logout,\
    inspecao_salvar_lote, inspecao_novo_lote, apaga_foto_1, apaga_foto_2, apaga_foto_3

urlpatterns = [
    path('', inspecao_index, name='inspecao_index'),
    path('lote', inspecao_lote, name='inspecao_lote'),
    path('editar', inspecao_editar, name='inspecao_editar'),
    path('finalizar', inspecao_finalizar, name='inspecao_finalizar'),
    path('logout', inspecao_logout, name='inspecao_logout'),
    path('salvar_lote', inspecao_salvar_lote, name='inspecao_salvar_lote'),
    path('novo_lote', inspecao_novo_lote, name='inspecao_novo_lote'),
    path('apaga_foto_1/<str:lote_num>/', apaga_foto_1, name='apaga_foto_1'),
    path('apaga_foto_2/<str:lote_num>/', apaga_foto_2, name='apaga_foto_2'),
    path('apaga_foto_3/<str:lote_num>/', apaga_foto_3, name='apaga_foto_3'),
]

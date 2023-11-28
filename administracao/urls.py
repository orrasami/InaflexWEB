from django.urls import path

from .views import table_list, table_detail, table_edit, table_new, administracao_login, administracao_logout

urlpatterns = [
    path('', administracao_login, name='administracao_login'),
    path('logout/', administracao_logout, name='administracao_logout'),
    path('tabelas/', table_list, name='table_list'),
    path('detalhes/<str:table_name>/', table_detail, name='table_detail'),
    path('editar/<str:table_name>/<int:pk>/', table_edit, name='table_edit'),
    path('novo/<str:table_name>/', table_new, name='table_new'),
]

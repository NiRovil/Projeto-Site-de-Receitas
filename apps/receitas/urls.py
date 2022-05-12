from django.urls import path
from .views import *

# Define as urls a serem atendidas pelas requisições.

urlpatterns = [
    path('', index, name='index'),
    path('receita/<int:receita_id>', receita, name='receita_id'),
    path('buscar', buscar, name='buscar'),
    path('criacao_receita', criacao_receita, name='criacao_receita'),
    path('deletar/<int:receita_id>', deleta_receita, name='deleta_receita'),
    path('editar/<int:receita_id>', editar_receita, name='editar_receita'),
    path('atualizar', atualizar_receita, name='atualizar_receita')
]

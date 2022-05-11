from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('logout', views.logout, name='logout'),
    path('criacao_receita', views.criacao_receita, name='criacao_receita'),
    path('deletar/<int:receita_id>', views.deleta_receita, name='deleta_receita'),
    path('editar/<int:receita_id>', views.editar_receita, name='editar_receita'),
    path('atualizar', views.atualizar_receita, name='atualizar_receita')
]
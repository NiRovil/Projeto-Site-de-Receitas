from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('receita/<int:receitas_id>', views.receita, name='receita_id'),
    path('buscar', views.buscar, name='buscar')
]

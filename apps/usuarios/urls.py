from django.urls import path
from . import views

# Define as urls a serem atendidas pelas requisições.

urlpatterns = [
    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('logout', views.logout, name='logout'),
]
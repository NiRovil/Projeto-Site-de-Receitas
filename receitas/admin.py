from re import search
from django.contrib import admin
from . models import Receita
# Register your models here.

class ModeloRegistro(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ('id', 'nome_receita')
    list_display_links = ('id', 'nome_receita')
    list_filter = ['categoria']
    search_fields = ['nome_receita']
    list_per_page = 10
=======
    list_display = ['id', 'nome_receita']
    list_display_links = ['id', 'nome_receita']
    list_filter = ['categoria']
    search_fields = ['nome_receita']
>>>>>>> 94ced0966f2dfee762659efd28a89c1e9c8d5dd8

admin.site.register(Receita, ModeloRegistro)
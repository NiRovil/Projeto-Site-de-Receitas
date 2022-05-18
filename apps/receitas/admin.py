from django.contrib import admin
from . models import Receita

# Define o que será mostrado para o usuário na pagina ADMIN.

class ModeloRegistro(admin.ModelAdmin):
    list_display = ['id', 'nome_receita', 'publicada']
    list_editable = ['publicada']
    list_display_links = ['id', 'nome_receita']
    list_filter = ['categoria']
    search_fields = ['nome_receita']

admin.site.register(Receita, ModeloRegistro)
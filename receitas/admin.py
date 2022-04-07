from django.contrib import admin
from .models import Receita
# Register your models here.

class ModeloRegistro(admin.ModelAdmin):
    list_display = ('id', 'nome_receita')
    list_display_links = ('id', 'nome_receita')
    list_filter = ['categoria']
    search_fields = ['nome_receita']
    list_per_page = 10

admin.site.register(Receita, ModeloRegistro)
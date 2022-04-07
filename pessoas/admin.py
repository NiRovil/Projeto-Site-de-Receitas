from django.contrib import admin
from . models import Pessoa
# Register your models here.
class ModeloRegistro(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email')
    list_display_links = ('id', 'nome')
    list_per_page = 10

admin.site.register(Pessoa, ModeloRegistro)
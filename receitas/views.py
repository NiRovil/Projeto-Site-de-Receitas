from django.shortcuts import get_object_or_404, get_list_or_404, render
from .models import Receita

def index(request):
    receitas = Receita.objects.all()
    dados = {
        'receitas':receitas
    }

    return render(request, 'index.html', dados)

def receita(request, receitas_id):
    receita = get_object_or_404(Receita, pk=receitas_id)
    lista = {'receitas' : receita}
    return render(request, 'receita.html', lista)
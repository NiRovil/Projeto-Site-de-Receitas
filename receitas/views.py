from django.shortcuts import get_object_or_404, get_list_or_404, render
from .models import Receita

def index(request):
    receitas = Receita.objects.order_by('-data_da_receita').filter(publicada=True)
    dados = {
        'receitas':receitas
    }

    return render(request, 'index.html', dados)

def receita(request, receitas_id):
    receita = get_object_or_404(Receita, pk=receitas_id)
    lista = {'receitas' : receita}
    return render(request, 'receita.html', lista)

def buscar(request):
    receita_a_buscar = Receita.objects.order_by('-data_da_receita').filter(publicada=True)

    if 'search' in request.GET:
        nome_a_buscar = request.GET['search']
        if nome_a_buscar:
            receita_a_buscar = receita_a_buscar.filter(nome_receita__icontains=nome_a_buscar)
    
    dados = {
        'receitas' : receita_a_buscar
    }

    return render(request, 'buscar.html', dados)
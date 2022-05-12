from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from receitas.models import Receita
from django.core.paginator import Paginator

# Define o que cada requisição vai atender.

def index(request):

    """Retorna a index com todas as receitas filtradas para o usuário."""

    receitas = Receita.objects.order_by('-data_da_receita').filter(publicada=True)

    # Define quantos itens serão exibidos por pagina e o numero da pagina que o usuário se encontra.
    paginator = Paginator(receitas, 3)
    page = request.GET.get('page')
    receitas_pagina = paginator.get_page(page)
    dados = {
        'receitas':receitas_pagina
    }

    return render(request, 'receitas/index.html', dados)

def receita(request, receita_id):

    """Retorna a receita selecionada pelo usuário."""

    # Busca a receita publicada por meio de seu ID.
    receita = get_object_or_404(Receita, pk=receita_id)
    lista = {'receitas' : receita}
    return render(request, 'receitas/receita.html', lista)

def buscar(request):

    """Retorna a receita filtrada pelo usuário."""

    receita_a_buscar = Receita.objects.order_by('-data_da_receita').filter(publicada=True)

    # Busca na requisição o que foi digitado na aba de busca pelo usuário.
    if 'search' in request.GET:
        nome_a_buscar = request.GET['search'] 
        if nome_a_buscar:
            receita_a_buscar = receita_a_buscar.filter(nome_receita__icontains=nome_a_buscar) 

    dados = {
        'receitas' : receita_a_buscar
    }

    return render(request, 'receitas/buscar.html', dados)

def criacao_receita(request):

    """Opção de criação de receita."""


    # Busca na requisição as variáveis digitadas pelo usuário.
    if request.method == 'POST':
        nome_receita = request.POST['nome_receita']
        ingredientes = request.POST['ingredientes']
        modo_preparo = request.POST['modo_preparo']
        tempo_preparo = request.POST['tempo_preparo']
        rendimento = request.POST['rendimento']
        categoria = request.POST['categoria']
        foto_da_receita = request.FILES['foto_receita']
        # Busca na requisição o ID do usuário que quer criar a receita.
        user = get_object_or_404(User, pk=request.user.id) 
        receita = Receita.objects.create(pessoa = user,nome_receita = nome_receita,
        ingredientes = ingredientes, modo_preparo = modo_preparo, tempo_preparo = tempo_preparo,
        rendimento = rendimento, categoria = categoria, foto_da_receita = foto_da_receita)
        receita.save()

        return redirect('dashboard')
    else:
        return render(request, 'receitas/criacao_receita.html')
    
def deleta_receita(request, receita_id):

    """Opção de deletar uma receita."""

    # Busca na requisição a receita a ser deletada por meio de seu ID.
    receita = get_object_or_404(Receita, pk=receita_id)
    receita.delete()
    return redirect('dashboard')

def editar_receita(request, receita_id):

    """Opção de editar uma receita."""

    # Busca na requisição a receita a ser editada por meio de seu ID.
    receita = get_object_or_404(Receita, pk=receita_id)
    edicao = {'receita':receita}
    return render(request, 'receitas/editar_receita.html', edicao)

def atualizar_receita(request):

    """Opção de atualização de uma receita."""

    # Busca na requisição as variáveis digitadas pelo usuário e substitui no modelo de objeto 'Receita'.
    if request.method == 'POST':
        receita_id = request.POST['receita_id']
        r = Receita.objects.get(pk=receita_id)
        r.nome_receita = request.POST['nome_receita'] 
        r.ingredientes = request.POST['ingredientes']
        r.modo_preparo = request.POST['modo_preparo']
        r.tempo_preparo = request.POST['tempo_preparo']
        r.rendimento = request.POST['rendimento']
        r.categoria = request.POST['categoria']
        if 'foto_da_receita' in request.FILES:
            r.foto_da_receita = request.FILES['foto_da_receita']
        r.save()

        return redirect('dashboard')
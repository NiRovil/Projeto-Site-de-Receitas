from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from receitas.models import Receita

def index(request):
    receitas = Receita.objects.order_by('-data_da_receita').filter(publicada=True)
    dados = {
        'receitas':receitas
    }

    return render(request, 'receitas/index.html', dados)

def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    lista = {'receitas' : receita}
    return render(request, 'receitas/receita.html', lista)

def buscar(request):
    receita_a_buscar = Receita.objects.order_by('-data_da_receita').filter(publicada=True)

    if 'search' in request.GET:
        nome_a_buscar = request.GET['search']
        if nome_a_buscar:
            receita_a_buscar = receita_a_buscar.filter(nome_receita__icontains=nome_a_buscar)
    
    dados = {
        'receitas' : receita_a_buscar
    }

    return render(request, 'receitas/buscar.html', dados)

def criacao_receita(request):
    if request.method == 'POST':
        nome_receita = request.POST['nome_receita']
        ingredientes = request.POST['ingredientes']
        modo_preparo = request.POST['modo_preparo']
        tempo_preparo = request.POST['tempo_preparo']
        rendimento = request.POST['rendimento']
        categoria = request.POST['categoria']
        foto_da_receita = request.FILES['foto_receita']
        user = get_object_or_404(User, pk=request.user.id)
        receita = Receita.objects.create(pessoa = user,nome_receita = nome_receita,
        ingredientes = ingredientes, modo_preparo = modo_preparo, tempo_preparo = tempo_preparo,
        rendimento = rendimento, categoria = categoria, foto_da_receita = foto_da_receita)
        receita.save()

        return redirect('dashboard')
    else:
        return render(request, 'receitas/criacao_receita.html')
    
def deleta_receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    receita.delete()
    return redirect('dashboard')

def editar_receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    edicao = {'receita':receita}
    return render(request, 'receitas/editar_receita.html', edicao)

def atualizar_receita(request):
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
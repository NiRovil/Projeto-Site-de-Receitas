from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_auth
from django.contrib.auth import logout as logout_auth
from receitas.models import Receita


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if email == "" or senha == "":
            return redirect('login')
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = authenticate(request, username=nome, password=senha)
            if user is not None:
                login_auth(request, user)
                print('Login realizado')
                return redirect('dashboard')
    return render(request, 'usuario/login.html')

def dashboard(request):
    if request.user.is_authenticated:
        idd = request.user.id
        receitas = Receita.objects.order_by('-data_da_receita').filter(pessoa=idd)
        dados = {'receitas':receitas}
        return render(request, 'usuario/dashboard.html', dados)
    else:
        return redirect('index')

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha_confirmacao = request.POST['password2']
        if not nome.strip():
            return redirect('cadastro')
        if not email.strip():
            return redirect('cadastro')
        if senha != senha_confirmacao:
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            return redirect('cadastro')
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        return redirect('login')
    else:
        return render(request, 'usuario/cadastro.html')

def logout(request):
    logout_auth(request)
    return redirect('index')

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
        return render(request, 'usuario/criacao_receita.html')
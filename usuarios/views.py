from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_auth, logout as logout_auth
from django.contrib import messages
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
            messages.error(request, 'Campo nome não pode estar em branco!')
            return redirect('cadastro')
        if not email.strip():
            messages.error(request, 'Campo email não pode estar em branco!')
            return redirect('cadastro')
        if senha != senha_confirmacao:
            messages.error(request, 'As senhas não coincidem!')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email já cadastrado!')
            return redirect('cadastro')
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        messages.success(request, 'Usuário cadastrado com sucesso!')
        return redirect('login')
    else:
        return render(request, 'usuario/cadastro.html')

def logout(request):
    logout_auth(request)
    return redirect('index')
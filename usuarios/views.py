from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['password']
        if email == "" or senha == "":
            return redirect('login')
        else:
            return redirect('dashboard')
    return render(request, 'usuario/login.html')

def dashboard(request):
    return render(request, 'usuario/dashboard.html')

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
        user = User.objects.create(username=nome, email=email, password=senha)
        user.save()
        return redirect('login')
    else:
        return render(request, 'usuario/cadastro.html')

def logout(request):
    pass
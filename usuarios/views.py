from django.shortcuts import render

def login(request):
    return render(request, 'usuario/login.html')

def dashboard(request):
    pass

def cadastro(request):
    return render(request, 'usuario/cadastro.html')

def logout(request):
    pass
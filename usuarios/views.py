from django.shortcuts import render, redirect

def login(request):
    return render(request, 'usuario/login.html')

def dashboard(request):
    pass

def cadastro(request):
    if request.method == 'POST':
        return redirect('login')
    else:
        return render(request, 'usuario/cadastro.html')

def logout(request):
    pass
from django.shortcuts import render

# Create your views here.
# TODA FUNÇÃO DENTRO DE VIEWS DEVE CONTER O PARÂMETRO REQUEST
def homepage(request):
    return render(request, 'homepage.html')

def loja(request):
    return render(request, 'loja.html')

def carrinho(request):
    return render(request, 'carrinho.html')

def checkout(request):
    return render(request, 'checkout.html')

def minha_conta(request):
    return render(request, 'usuario/minhaconta.html')

def login(request):
    return render(request, 'usuario/login.html')
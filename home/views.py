from django.shortcuts import render


def index(request):
    return render(request, 'home/index.html')


def inspecao(request):
    return render(request, 'inspecao/index.html')


def recebimento(request):
    return render(request, 'recebimento/index.html')


def liberacao_pedidos(request):
    return render(request, 'liberacao_pedidos/index.html')


def administracao(request):
    return render(request, 'administracao/index.html')

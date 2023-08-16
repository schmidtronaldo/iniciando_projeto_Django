
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def imagem(request):
    return render(request, 'imagem.html')
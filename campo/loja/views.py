from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def cadastrar(request):

    return HttpResponse("Opa! Estou no cadastrar")


def atualizar(request):

    return HttpResponse("Opa! Estou no atualizar")



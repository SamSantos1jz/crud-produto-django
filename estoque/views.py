from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Produto
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/auth/login/")
def cadastrar_produto(request):
    if request.method == "GET":
        return render(request, 'cadastrar_produto.html')
    elif request.method == "POST":
        var_nome = request.POST.get('nome')
        var_preco = request.POST.get('preco')
        var_valiade = request.POST.get('validade')
        var_quantidade = request.POST.get('quantidade')
        
        produto = Produto(
            nome = var_nome,
            preco = var_preco,
            validade = var_valiade,
            quantidade = var_quantidade
        )
        
        produto.save()
        return redirect('/estoque/cadastrar_produto')
    
@login_required(login_url="/auth/login/")
def listar_produto(request):
    produtos = Produto.objects.filter().all
    return render(request,'listar_produto.html', {'produtos':produtos})

@login_required(login_url="/auth/login/")
def deletar_produto(request, id):
    produto = Produto.objects.get(id=id)
    produto.delete()
    return redirect('/estoque/listar_produto/')


from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login 
from django.contrib.auth.decorators import login_required

# Create your views here.
def cadastro_usuario(request):
    if request.method=="GET":
        return render(request, "cadastro.html")
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        email = request.POST.get('email')
        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse("Usuario ou email já existente")
        
        user = User.objects.create_user(username=username, password=senha, email=email)
        user.save()
        return HttpResponse("Usuario Cadastrado com sucesso!")

def login_usuario(request):
    if request.method =="GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        user = authenticate(username=username, password=senha)

        if user: 
            login(request, user)
            return redirect('/estoque/listar_produto/')
        else:
           return HttpResponse("Username e senha não estão certas")
        

       
           


   

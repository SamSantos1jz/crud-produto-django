from django.urls import path 
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro_usuario, name="cadastro"),
    path('login/', views.login_usuario, name="login"),
]
    
from django.shortcuts import render,redirect
# esto me indica que debo logearme antes de entrar a un vista
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.

def Home(request):
    return render(request,'core/home.html')

# con esto le digo que antes de entra a esta vista debo estar logeado
@login_required
def Products(request):
    return render(request,'core/products.html')

def Exit(request):
    logout(request)
    return redirect('home')
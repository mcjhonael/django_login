from django.urls import path
from .views import Home,Products,Exit

urlpatterns = [
    path('',Home,name='home'),
    path('products/',Products,name='products'),
    path('logout/',Exit,name='exit'),
]

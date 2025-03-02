from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_principal, name='menu_principal'),  #Menú principal
    path('euler-mejorado/', views.calcular_euler_mejorado, name='euler_mejorado'),
    path('newton-raphson/', views.calcular_newton_raphson, name='newton_raphson'),
    path('runge-kutta/', views.calcular_runge_kutta, name='runge_kutta'),
]
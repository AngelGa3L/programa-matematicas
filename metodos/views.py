from django.shortcuts import render
from math import *

def menu_principal(request):
    return render(request, 'desing/menu_principal.html')

# Create your views here.

#EULER MEJORADO
def euler_mejorado(f, x0, y0, h, xf):
    resultados = []
    x = x0
    y = y0
    n = 0
    while x < xf + h / 2:
        y_pred = y + h * eval(f, {'x': x, 'y': y})
        y_corr = y + h/2 * (eval(f, {'x': x, 'y': y}) + eval(f, {'x': x + h, 'y': y_pred}))
        resultados.append((n, x, y, y_pred))
        y = y_corr
        x = x + h
        n += 1
    return resultados

def calcular_euler_mejorado(request):
    resultados = None
    
    if request.method == 'POST':
        try:
            f = request.POST.get('funcion')
            x0 = float(request.POST.get('x0'))
            y0 = float(request.POST.get('y0'))
            h = float(request.POST.get('h'))
            xf = float(request.POST.get('xf'))

            resultados = euler_mejorado(f, x0, y0, h, xf)
        except Exception as e:
            return render(request, 'euler-mejorado/euler_mejorado.html', {'error': str(e)})

    return render(request, 'euler-mejorado/euler_mejorado.html', {'resultados': resultados})


#NEWTON-RAPSHON
def newton_raphson(func, x0, decimales):
    def f(x):
        return eval(func, {'x': x})
    
    def df(x):
        h = 1e-5
        return (f(x + h) - f(x - h)) / (2 * h)
    
    resultados = []
    tolerancia = 10 ** (-decimales)
    iteracion = 0
    while True:
        fx = f(x0)
        dfx = df(x0)
        if dfx == 0:
            raise ValueError("La derivada es cero. No se puede continuar.")
        x1 = x0 - fx / dfx
        
        resultados.append((iteracion, round(x0, decimales), round(fx, decimales), round(dfx, decimales), round(x1, decimales)))
        
        if abs(x1 - x0) < tolerancia:
            break
        x0 = x1
        iteracion += 1
    
    return resultados

def calcular_newton_raphson(request):
    resultados = None
    if request.method == 'POST':
        try:
            func = request.POST.get('funcion')
            x0 = float(request.POST.get('x0'))
            decimales = int(request.POST.get('decimales'))

            resultados = newton_raphson(func, x0, decimales)
        except Exception as e:
            return render(request, 'newton-raphson/newton_raphson.html', {'error': str(e)})

    return render(request, 'newton-raphson/newton_raphson.html', {'resultados': resultados})

#RUNGE KUTTA 4TO ORDEN

def runge_kutta_4th_order(func, x0, y0, h, xf):
    resultados = []
    xn = x0
    yn = y0
    n = 0

    while xn < xf + h / 2:
        k1 = h * eval(func, {"x": xn, "y": yn})
        k2 = h * eval(func, {"x": xn + h/2, "y": yn + k1/2})
        k3 = h * eval(func, {"x": xn + h/2, "y": yn + k2/2})
        k4 = h * eval(func, {"x": xn + h, "y": yn + k3})

        yn1 = yn + (k1 + 2*k2 + 2*k3 + k4) / 6  # Actualizar y

        resultados.append((n, round(xn, 5), round(yn, 5), 
                          round(k1, 5), round(k2, 5), 
                          round(k3, 5), round(k4, 5), 
                          round(yn1, 5)))

        yn = yn1
        xn += h
        n += 1

    return resultados

def calcular_runge_kutta(request):
    resultados = None
    if request.method == 'POST':
        try:
            func = request.POST.get('funcion')
            x0 = float(request.POST.get('x0'))
            y0 = float(request.POST.get('y0'))
            h = float(request.POST.get('h'))
            xf = float(request.POST.get('xf'))

            resultados = runge_kutta_4th_order(func, x0, y0, h, xf)
        except Exception as e:
            return render(request, 'runge-kutta/runge_kutta.html', {'error': str(e)})

    return render(request, 'runge-kutta/runge_kutta.html', {'resultados': resultados})
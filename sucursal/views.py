from django.shortcuts import render

from .models import Producto
# from Tienda.sucursal.models import Producto

# Create your views here.

def index(request):
    # ORM
    productos = Producto.objects.all()
    print(productos)
    context = {
        "productos" : productos,
        "mensaje" : 'hola como estas',
        "dinero" : 123123
    }

    return render(request, 'producto/index.html', context)

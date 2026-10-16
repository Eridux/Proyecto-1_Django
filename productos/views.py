from django.shortcuts import render

# Create your views here.
def listado_productos(request):
    datos: dict[str,str] = {
        'titulo': 'Lista de productos',
        'encabezado': 'Ver listado de Productos'
    }
    
    return render(request, 'productos/listado.html', datos)
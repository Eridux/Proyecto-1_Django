from django.shortcuts import render

# Create your views here.
def listado_clientes(request):
    datos: dict[str,str] = {
        'titulo': 'Lista de clientes',
        'encabezado': 'Ver listado de clientes'
    }
    
    return render(request, 'clientes/listado.html', datos)
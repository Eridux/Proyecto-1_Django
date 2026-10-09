from django.shortcuts import render

# Create your views here.
def listado_empleados(request):
    datos: dict[str,str] = {
        'titulo': 'Lista de empleados',
        'encabezado': 'Ver listado de empleados'
    }
    
    return render(request, 'empleados/listado.html', datos)
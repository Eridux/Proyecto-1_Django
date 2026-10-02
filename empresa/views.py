from django.shortcuts import render

# Create your views here.
def inicio(request):
    datos: dict[str,str] = {
        'titulo': 'Página de inicio',
        'encabezado': 'Bienvenidos a la página de inicio de la empresa',
    }
    return render(request, 'empresa/index.html', datos)
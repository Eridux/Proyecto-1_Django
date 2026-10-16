from django.shortcuts import render

type Valor = str | list

# Create your views here.
def listado_clientes(request):
    clientes: list[str] = [
        'Ferreteria C.A',
        'Licoreria S.R.L',
        'Papeleria C.A',
        'Ferretubo S.R.L',
        'Pizzeria Mario C.A',
        'Tienda Mascotas S.R.L',
    ]
    
    datos: dict[str,Valor] = {
        'titulo': 'Lista de clientes',
        'encabezado': 'Ver listado de Clientes',
        'clientes': clientes
    }
    
    return render(request, 'clientes/listado.html', datos)
from django.shortcuts import render,redirect
from .models import Marca, Automovil
# Create your views here.
from django.contrib.auth.decorators import login_required
#importamos el decorador login_required
#un decorador es una funcion que extiende la funcionalidad
#de un metodo inyectandole mas codigo


def home(request):
    return render(request, 'core/home.html')

def galeria(request):
    return render(request, 'core/galeria.html')

@login_required
def agregar_auto(request):
    marcas  = Marca.objects.all()
    #enviamos las marcas hacia el template
    variables = {
        'marcas':marcas
    }

    #preguntaremos si es POST
    if request.POST:
        #si la peticion es POST obtendremos los datos
        auto = Automovil()
        auto.patente = request.POST.get('txtPatente')
        auto.modelo = request.POST.get('txtModelo')
        auto.anio  = request.POST.get('txtAnio')
        #la marca es una colaboracion de clases
        #por lo tanto para obtener el combo primero
        #crearemos un objeto Marca
        marca = Marca()
        marca.id  = request.POST.get('cboMarca')
        #guardamos la marca completo dentro del auto
        auto.marca = marca

        #procedemos a guardar el auto en la BBDD
        try:
            auto.save()
            variables['mensaje'] = "Guardado correctamente"
        except:
            variables['mensaje'] = "No se ha podido guardar"

    return render(request, 'core/agregar_auto.html', variables)

def listar_autos(request):

    autos = Automovil.objects.all()

    variables = {
        'autos':autos
    }

    return render(request, 'core/listar_autos.html', variables)

def eliminar_auto(request, id):
    #primer paso buscamos el automovil
    auto = Automovil.objects.get(id=id)

    #procedemos a eliminar
    auto.delete()
    
    #redirigimos al usuario de vuelta al listado
    return redirect('listar_autos')


# capa de vista/presentación

from django.shortcuts import redirect, render
from .layers.services import services
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .layers.transport.transport import getAllImages 
from .layers.services.services import filterByType
from .layers.services.services import filterByCharacter

def spinner(request):
    return render(request, 'spinner.html')

def index_page(request):
    return render(request, 'index.html')

# esta función obtiene 2 listados: uno de las imágenes de la API y otro de favoritos, ambos en formato Card, y los dibuja en el template 'home.html'.
def home(request):
    images = getAllImages()  # obtiene todas las imágenes de la API.

    favourite_list = []

    return render(request, 'home.html', { 'images': images, 'favourite_list': favourite_list,})

# función utilizada en el buscador.
def search(request):
    name = request.POST.get('query', '')

    # si el usuario ingresó algo en el buscador, se deben filtrar las imágenes por dicho ingreso.
    if (name != ''):
        dataFiltered = filterByCharacter(name)
        favourite_list = []
        return render(request, 'home.html', { 'images': dataFiltered, 'favourite_list': favourite_list })
    else:
        return redirect('home')

# función utilizada para filtrar por el tipo del Pokemon
def filter_by_type(request):
    type = request.POST.get('type', '')
    getPokemos = "" # obtiene los pokemons filtrados por el tipo.
    if type != '':
        # retorna las imagenes filtradas por el tipo.
        images = filterByType(type)
        favourite_list = []
        
        return render(request, 'home.html', { 'images': images, 'favourite_list': favourite_list })
    else:
        return redirect('home')



# Estas funciones se usan cuando el usuario está logueado en la aplicación.
@login_required
def getAllFavouritesByUser(request):
    pass

@login_required
def saveFavourite(request):
    pass

@login_required
def deleteFavourite(request):
    pass

@login_required
def exit(request):
    logout(request)
    return redirect('home')
# capa de vista/presentación

from django.shortcuts import redirect, render, get_object_or_404
from .layers.services import services
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .layers.transport.transport import getAllImages 
from .layers.services.services import filterByType
from .layers.services.services import filterByCharacter
from .models import Favourite
from django.views.decorators.http import require_POST


def spinner(request):
    return render(request, 'spinner.html')

def index_page(request):
    return render(request, 'index.html')

# esta función obtiene 2 listados: uno de las imágenes de la API y otro de favoritos, ambos en formato Card, y los dibuja en el template 'home.html'.
def home(request):
    images = getAllImages()  # Tu función para obtener Pokémon de la API

    favourite_list = []
    if request.user.is_authenticated:
        favourite_list = Favourite.objects.filter(user=request.user).values_list('name', flat=True)

    return render(request, 'home.html', {
        'images': images,
        'favourite_list': favourite_list,
    })

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
def getAllFavouritesByUser(request):
    favourite_list = Favourite.objects.filter(user=request.user)
    context = {
        'favourite_list': favourite_list
    }
    return render(request, 'favourites.html', context)

@login_required
@require_POST
def saveFavourite(request):
    favourite, created = Favourite.objects.get_or_create(
        pokeapi_id=request.POST['id'],
        user=request.user,
        defaults={
            'name': request.POST['name'],
            'height': request.POST['height'],
            'weight': request.POST['weight'],
            'base_experience': request.POST['base_experience'],
            'image': request.POST['image'],
        }
    )
    return redirect(request.META.get('HTTP_REFERER', 'home'))

@login_required
@require_POST
def deleteFavourite(request):
    favourite_id = request.POST.get('id')
    favourite = get_object_or_404(Favourite, id=favourite_id, user=request.user)
    favourite.delete()
    return redirect(request.META.get('HTTP_REFERER', 'home'))

@login_required
def exit(request):
    logout(request)
    return redirect('home')
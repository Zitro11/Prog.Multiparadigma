from django.shortcuts import render
from .models import Artista,Album,Cancion,Discografia,Playlist,Premio
# Create your views here.

def pagina_inicio(request):
    return render(request, 'index.html')

def lista_artistas(request):
    artistas = Artista.objects.all()
    return render(request, 'artistas.html',{'artistas':artistas})

def lista_albums(request):
    albums = Album.objects.all()
    return render(request, 'albums.html',{'albums':albums})

def lista_canciones(request):
    canciones = Cancion.objects.all()
    return render(request, 'canciones.html', {'canciones':canciones})

def lista_discografias(request):
    discografias = Discografia.objects.all()
    return render(request, 'discografias.html', {'discografias':discografias})

def lista_playlists(request):
    playlists = Playlist.objects.all()
    return render(request, 'playlists.html', {'playlists':playlists})

def lista_premios(request):
    premios = Premio.objects.all()
    return render (request, 'premios.html', {'premios':premios})
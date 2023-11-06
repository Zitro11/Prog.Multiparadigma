"""
URL configuration for proyecto_musica project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from spotifyapp.views import lista_artistas, lista_albums, lista_canciones, lista_discografias, lista_playlists, lista_premios, pagina_inicio

urlpatterns = [
    path('',pagina_inicio, name='inicio'),   
    path('admin/', admin.site.urls),
    path('artistas/', lista_artistas, name='artistas'),
    path('albums/', lista_albums, name='albums'),
    path('canciones/', lista_canciones, name='canciones'),
    path('discografias/', lista_discografias, name='discografias'),
    path('playlists/', lista_playlists, name='playlists'),
    path('premios/', lista_premios, name='premios'),
]

from django.contrib import admin
from .models import Album,Artista,Cancion,Playlist,Discografia,Premio
# Register your models here.

admin.site.register(Album)
admin.site.register(Artista)
admin.site.register(Cancion)
admin.site.register(Playlist)
admin.site.register(Discografia)
admin.site.register(Premio)
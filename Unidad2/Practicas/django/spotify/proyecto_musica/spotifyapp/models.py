from django.db import models

# Create your models here.

class Artista(models.Model):
    nombre = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    edad = models.IntegerField()
    def __str__(self) -> str:
        return self.nombre

class Album(models.Model):
    titulo = models.CharField(max_length=100)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    año_publicacion = models.IntegerField()
    canciones = models.IntegerField()
    def __str__(self) -> str:
        return self.titulo

class Cancion(models.Model):
    titulo = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    duracion = models.DurationField()
    produccion = models.CharField(max_length=100)

class Playlist(models.Model):
    nombre = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    canciones = models.IntegerField()

class Discografia(models.Model):
    nombre = models.CharField(max_length=100)
    fundacion = models.IntegerField()
    sede = models.CharField(max_length=100)

class Premio(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
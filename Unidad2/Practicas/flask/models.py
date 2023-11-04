from database import db

class Actor(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.String(250))
    apellido=db.Column(db.String(250))
    sexo=db.Column(db.String(100))

class Director(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.String(250))
    apellido=db.Column(db.String(250))
    pais=db.Column(db.String(250))

class Pelicula(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.String(250))
    duracion=db.Column(db.Integer)
    genero=db.Column(db.String(250))
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class ActorForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    apellido = StringField('Apellido', validators=[DataRequired()])
    sexo = StringField('Sexo', validators=[DataRequired()])
    enviar = SubmitField('Enviar')

class DirectorForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    apellido = StringField('Apellido', validators=[DataRequired()])
    pais = StringField('País', validators=[DataRequired()])
    enviar = SubmitField('Enviar')

class PeliculaForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    duracion = IntegerField('Duración', validators=[DataRequired()])
    categoria = StringField('Categoría', validators=[DataRequired()])
    enviar = SubmitField('Enviar')

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField, SelectField, IntegerField, EmailField, PasswordField, RadioField
from wtforms.validators import DataRequired

class PokemonForm(FlaskForm):
    nombre = StringField("Nombre: ", validators=[DataRequired()])
    tipo = StringField("Tipo: ", validators=[DataRequired()])
    item = StringField("Item: ", validators=[DataRequired()])
    habilidad = StringField("Habilidad: ", validators=[DataRequired()])
    naturaleza = StringField("Naturaleza: ", validators=[DataRequired()])
    sprite_icon = StringField("Sprite-icon: ", validators=[DataRequired()])
    sprite_front = StringField("Sprite-front: ", validators=[DataRequired()])
    movimiento1 = StringField("Movimiento 1: ", validators=[DataRequired()])
    movimiento2 = StringField("Movimiento 2: ", validators=[DataRequired()])
    movimiento3 = StringField("Movimiento 3: ", validators=[DataRequired()])
    movimiento4 = StringField("Movimiento 4: ", validators=[DataRequired()])
    nombre_entrenador = HiddenField("Nombre del entrenador")
    enviar = SubmitField("Enviar")

class TeamForm(FlaskForm):
    nombredelequipo = StringField("Nombre del equipo: ", validators=[DataRequired()])
    nombre_entrenador = HiddenField("Nombre del entrenador")
    id_pokemon1 = IntegerField("ID del pokemon 1: ", validators=[DataRequired()])
    id_pokemon2 = IntegerField("ID del pokemon 2: ", validators=[DataRequired()])
    id_pokemon3 = IntegerField("ID del pokemon 3: ", validators=[DataRequired()])
    id_pokemon4 = IntegerField("ID del pokemon 4: ", validators=[DataRequired()])
    id_pokemon5 = IntegerField("ID del pokemon 5: ", validators=[DataRequired()])
    id_pokemon6 = IntegerField("ID del pokemon 6: ", validators=[DataRequired()])
    enviar = SubmitField("Enviar")

class TrainerForm(FlaskForm):
    nombre = StringField("Nombre: ", validators=[DataRequired()])
    password = PasswordField("Password: ")
    admin = RadioField("Administrador: ", choices=[(True, "Si"), (False, "No")])
    enviar = SubmitField("Enviar")
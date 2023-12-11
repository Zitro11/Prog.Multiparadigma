from flask import Blueprint,request,jsonify,render_template,redirect, url_for
from sqlalchemy import exc 
from models import Pokemon
from forms import PokemonForm
from app import db, flash

apppokemon = Blueprint('apppokemon', __name__, template_folder="templates")

@apppokemon.route('/pokemon')
def Index():
    Pokemons = Pokemon.query.all()
    return render_template("indexPokemon.html", pokemon = Pokemons)

@apppokemon.route('/pokemon/404')
def Error():
    return render_template('errorPokemon.html')

@apppokemon.route('/pokemon/add', methods = ["GET", "POST"])
def Agregar():
    try:
        pokemon = Pokemon()
        formPokemon = PokemonForm(obj = pokemon)
        if request.method == "POST":
            if formPokemon.validate_on_submit():
                formPokemon.populate_obj(pokemon)
                db.session.add(pokemon)
                db.session.commit()
                return redirect(url_for('apppokemon.Index'))
        return render_template('agregarPokemon.html', nuevoPkm = formPokemon)
    except Exception as ex:
        print(str(ex))
        return redirect(url_for('apppokemon.Error'))

@apppokemon.route('/pokemon/edit/<int:id>', methods = ["GET", "POST"])
def Editar(id):
    try:
        pokemon = Pokemon.query.get_or_404(id)
        formPokemon = PokemonForm(obj = pokemon)
        if request.method == "POST":
            if formPokemon.validate_on_submit():
                formPokemon.populate_obj(pokemon)
                db.session.commit()
                return redirect(url_for('apppokemon.Index'))
        return render_template('editarPokemon.html', editarPkm = formPokemon)
    except Exception as ex:
        print(str(ex))
        return redirect(url_for('apppokemon.Error'))

@apppokemon.route('/pokemon/delete/<int:id>', methods = ["GET"])
def Eliminar(id):
    try:
        pokemon = Pokemon.query.filter_by(id = id).first()
        db.session.delete(pokemon)
        db.session.commit()
        return redirect(url_for('apppokemon.Index'))
    except Exception as ex:
        print(str(ex))
        return redirect(url_for('apppokemon.Error'))

@apppokemon.route('/pokemon/json', methods = ["GET"])
def IndexJson():
    try:
        pokemons = Pokemon.query.order_by("id").all()
        lista = []
        for p in pokemons:
            d = {}
            d["id"] = p.id
            d["nombre"] = p.nombre
            d["tipo"] = p.tipo
            d["item"] = p.item
            d["habilidad"] = p.habilidad
            d["naturaleza"] = p.naturaleza
            d["sprite_icon"] = p.sprite_icon
            d["sprite_front"] = p.sprite_front
            d["movimiento1"] = p.movimiento1
            d["movimiento2"] = p.movimiento2
            d["movimiento3"] = p.movimiento3
            d["movimiento4"] = p.movimiento4
            d["id_entrenador"] = p.id_entrenador
            lista.append(d)
        return jsonify({"status":200, "pokemons":lista})
    except Exception as ex:
        print(str(ex))
        return jsonify({"status":500, "message": "Ocurrio un error", "error":str(ex)})
    
@apppokemon.route('/pokemon/json', methods = ["POST"])
def AgregarJson():
    try:
        if request.method == "POST":
            json = request.get_json()
            pokemon = Pokemon()
            pokemon.nombre = json["nombre"]
            pokemon.tipo = json["tipo"]
            pokemon.item = json["item"]
            pokemon.habilidad = json["habilidad"]
            pokemon.naturaleza = json["naturaleza"]
            pokemon.sprite_icon = json["sprite_icon"]
            pokemon.sprite_front = json["sprite_front"]
            pokemon.movimiento1 = json["movimiento1"]
            pokemon.movimiento2 = json["movimiento2"]
            pokemon.movimiento3 = json["movimiento3"]
            pokemon.movimiento4 = json["movimiento4"]
            pokemon.id_entrenador = json["id_entrenador"]
            db.session.add(pokemon)
            db.session.commit()
            return jsonify({"status":200, "Message":"Pokemon Agregado Correctamente"})
    except Exception as ex:
        print(str(ex))
        return jsonify({"status":500, "message": "Ocurrio un error", "error":str(ex)})

@apppokemon.route('/pokemon/json', methods=["PUT"])
def EditarJson():
    try:
        json = request.get_json()
        pokemon = Pokemon.query.get_or_404(json["id"])
        pokemon.nombre = json["nombre"]
        pokemon.tipo = json["tipo"]
        pokemon.item = json["item"]
        pokemon.habilidad = json["habilidad"]
        pokemon.naturaleza = json["naturaleza"]
        pokemon.movimiento1 = json["movimiento1"]
        pokemon.movimiento2 = json["movimiento2"]
        pokemon.movimiento3 = json["movimiento3"]
        pokemon.movimiento4 = json["movimiento4"]
        pokemon.id_entrenador = json["id_entrenador"]
        db.session.commit()
        return jsonify({"status":200, "message":"Pokemon Actualizado Correctamente"})
    except Exception as ex:
        print(str(ex))
        return jsonify({"status":500, "message": "Ocurrio un error", "error":str(ex)})

@apppokemon.route('/pokemon/json', methods = ["DELETE"])
def EliminarJson():
    try:
        json = request.get_json()
        pokemon = Pokemon.query.get_or_404(json['id'])
        db.session.delete(pokemon)
        db.session.commit()
        return jsonify({"status":200, "message":"Pokemon Eliminado Correctamente"})
    except Exception as ex:
        print(str(ex))
        return jsonify({"status":500, "message": "Ocurrio un error", "error":str(ex)})
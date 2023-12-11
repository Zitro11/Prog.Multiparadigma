from flask import Blueprint,request,jsonify,render_template,redirect, url_for
from sqlalchemy import exc 
from models import Team
from forms import TeamForm
from app import db, flash

appteam = Blueprint('appteam', __name__, template_folder="templates")

@appteam.route('/equipo')
def Index():
    equipos = Team.query.all()
    print(equipos)
    return render_template("indexEquipo.html", teams = equipos)

@appteam.route('/equipo/404')
def Error():
    return render_template('errorEquipo.html')

@appteam.route('/equipo/add', methods = ["GET", "POST"])
def Agregar():
    try:
        equipo = Team()
        newEquipo = TeamForm(obj = Team)
        if request.method == "POST":
            if newEquipo.validate_on_submit():
                newEquipo.populate_obj(equipo)
                db.session.add(equipo)
                db.session.commit()
                return redirect(url_for('appteam.Index'))
        return render_template('agregarEquipo.html', nuevoTeam = newEquipo)
    except Exception as ex:
        print(str(ex))
        return redirect(url_for('appteam.Error'))

@appteam.route('/equipo/edit/<int:id>', methods = ["GET", "POST"])
def Editar(id):
    try:
        equipo = Team.query.get_or_404(id)
        editequipo = TeamForm(obj = equipo)
        if request.method == "POST":
            if editequipo.validate_on_submit():
                editequipo.populate_obj(equipo)
                db.session.commit()
                return redirect(url_for('appteam.Index'))
        return render_template('editarEquipo.html', editarTeam = editequipo)
    except Exception as ex:
        print(str(ex))
        return redirect(url_for('appteam.Error'))

@appteam.route('/equipo/delete/<int:id>')
def Eliminar(id):
    try:
        equipo = Team.query.filter_by(id = id).first()
        db.session.delete(equipo)
        db.session.commit()
        return redirect(url_for('appteam.Index'))
    except Exception as ex:
        print(str(ex))
        return redirect(url_for('appteam.Error'))

@appteam.route('/equipo/json', methods = ["GET"])
def IndexJson():
    try:
        equipos = Team.query.order_by("id").all()
        lista = []
        for e in equipos:
            d = {}
            d["id"] = e.id
            d["nombredelequipo"] = e.nombredelequipo
            d["id_entrenador"] = e.id_entrenador
            d["id_pokemon1"] = e.id_pokemon1
            d["id_pokemon2"] = e.id_pokemon2
            d["id_pokemon3"] = e.id_pokemon3
            d["id_pokemon4"] = e.id_pokemon4
            d["id_pokemon5"] = e.id_pokemon5
            d["id_pokemon6"] = e.id_pokemon6
            lista.append(d)
        return jsonify({"status":200, "Equipos":lista})
    except Exception as ex:
        print(str(ex))
        return jsonify({"status":500, "message": "Ocurrio un error", "error":str(ex)})
    
@appteam.route('/equipo/json', methods = ["POST"])
def AgregarJson():
    try:
        if request.method == "POST":
            json = request.get_json()
            equipo = Team()
            equipo.nombredelequipo = json["nombredelequipo"]
            equipo.id_entrenador = json["id_entrenador"]
            equipo.id_pokemon1 = json["id_pokemon1"]
            equipo.id_pokemon2 = json["id_pokemon2"]
            equipo.id_pokemon3 = json["id_pokemon3"]
            equipo.id_pokemon4 = json["id_pokemon4"]
            equipo.id_pokemon5 = json["id_pokemon5"]
            equipo.id_pokemon6 = json["id_pokemon6"]
            db.session.add(equipo)
            db.session.commit()
            return jsonify({"status":200, "Message":"Equipo Agregado Correctamente"})
    except Exception as ex:
        print(str(ex))
        return jsonify({"status":500, "message": "Ocurrio un error", "error":str(ex)})

@appteam.route('/equipo/json', methods=["PUT"])
def EditarJson():
    try:
        json = request.get_json()
        equipo = Team.query.get_or_404(json["id"])
        equipo.nombredelequipo = json["nombredelequipo"]
        equipo.id_entrenador = json["id_entrenador"]
        equipo.id_pokemon1 = json["id_pokemon1"]
        equipo.id_pokemon2 = json["id_pokemon2"]
        equipo.id_pokemon3 = json["id_pokemon3"]
        equipo.id_pokemon4 = json["id_pokemon4"]
        equipo.id_pokemon5 = json["id_pokemon5"]
        equipo.id_pokemon6 = json["id_pokemon6"]
        db.session.commit()
        return jsonify({"status":200, "message":"Equipo Actualizado Correctamente"})
    except Exception as ex:
        print(str(ex))
        return jsonify({"status":500, "message": "Ocurrio un error", "error":str(ex)})

@appteam.route('/equipo/json', methods = ["DELETE"])
def EliminarJson():
    try:
        json = request.get_json()
        equipo = Team.query.get_or_404(json['id'])
        db.session.delete(equipo)
        db.session.commit()
        return jsonify({"status":200, "message":"Equipo Eliminado Correctamente"})
    except Exception as ex:
        print(str(ex))
        return jsonify({"status":500, "message": "Ocurrio un error", "error":str(ex)})
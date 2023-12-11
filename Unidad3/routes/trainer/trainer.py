from flask import Blueprint,request,jsonify,render_template,redirect, url_for
from sqlalchemy import exc, select, desc
from models import Trainer, Pokemon, Team
from forms import TrainerForm
from app import db,bcrypt
from auth import tokenCheck,verificar

apptrainer=Blueprint('apptrainer',__name__,template_folder="templates")
# @appuser.route("/")
# def index():
#     return render_template("index.html")

@apptrainer.route('/404')
def error():
    return render_template("error.html"), 404

@apptrainer.errorhandler(500)
def internal_server_error(error):
    return render_template('error.html'), 500

@apptrainer.route("/auth/registro",methods=["POST"])
def registro():
    trainer = request.get_json()
    trainerExists=Trainer.query.filter_by(nombre=trainer['nombre']).first()
    if not trainerExists:
        trainer=Trainer(nombre=trainer['nombre'],password=trainer['password'])
        try:
            db.session.add(trainer)
            db.session.commit()
            mensaje="Entrenador Creado"
        except exc.SQLAlchemyError as e:
            mensaje="ERROR "+e
    return jsonify({"message":mensaje})

@apptrainer.route('/auth/login',methods=["POST"])
def login():
    try:
        trainer = request.get_json()
        entrenador = Trainer(nombre=trainer['nombre'],password=trainer['password'])
        searchTrainer = Trainer.query.filter_by(nombre=entrenador.nombre).first()
        if searchTrainer:
            validation = bcrypt.check_password_hash(searchTrainer.password,trainer["password"])
            if validation:
                auth_token=entrenador.encode_auth_token(user_id=searchTrainer.id)
                response = {
                    'status':'success',
                    'message':'Login exitoso',
                    'auth_token':auth_token
                }
                print(response)
                return jsonify(response)
        return jsonify({"status":300,"message":"Datos incorrectos"})
    except Exception as ex:
        return jsonify({"status":400, "message":"Ha ocurrido un incidente", "error": str(ex)})

@apptrainer.route('/entrenador/json',methods=['GET'])
@tokenCheck
def getTrainer(entrenador):
    print(entrenador)
    print(entrenador['admin'])
    if entrenador['admin']:
        output=[]
        entrenadores=Trainer.query.all()
        for entrenador in entrenadores:
            entrenadorData={}
            entrenadorData['id']=entrenador.id
            entrenadorData['nombre']=entrenador.nombre
            entrenadorData['password']=entrenador.password
            entrenadorData['registered_on']=entrenador.registered_on
            output.append(entrenadorData)
        return jsonify({'entrenadores':output})
    else:
        return jsonify({'Error':"No tienes permisos"})

@apptrainer.route('/entrenador/json', methods=["PUT"])
@tokenCheck
def UpdateTrainer(entrenador):
    try:
        json = request.get_json()
        trainer = Trainer.query.filter_by(nombre=json["nombre"]).first()
        if trainer:
            trainer.nombre = json["nombre"]
            trainer.password = Trainer.encodePassword(json["password"])
            trainer.admin = json["admin"]
            db.session.commit()
            return jsonify({"status":200, "message":"Entrenador actualizado"})
        else:
            return jsonify({"status":400, "message":"Entrenador no encontrado"})
    except Exception as ex:
        return jsonify({"status":500, "message":"Ha ocurrido un incidente", "error": str(ex)})
    
@apptrainer.route('/entrenador/json', methods=["DELETE"])
@tokenCheck
def DeleteUser(entrenador):
    try:
        json = request.get_json()
        trainer = Trainer.query.filter_by(id=json["id"]).first()
        if trainer:
            db.session.delete(trainer)
            db.session.commit()
            return jsonify({"status":200, "message":"Entrenador eliminado"})
        else:
            return jsonify({"status":400, "message":"Entrenador no encontrado"})
    except Exception as ex:
        return jsonify({"status":500, "message":"Ha ocurrido un incidente", "error": str(ex)})

@apptrainer.route('/')
def Index():
    return render_template('login.html')

@apptrainer.route('/main')
def main():
    try:
        equiposAll = Team.query.order_by(desc("id")).all()
        pokemonAll = Pokemon.query.order_by(desc("id")).all()
        trainer = Trainer.query.order_by(desc("id")).limit(3).all()
        equipos = Team.query.order_by(desc("id")).limit(3).all()
        pokemon = Pokemon.query.order_by(desc("id")).limit(3).all()
        
        return render_template('main.html', equipos = equiposAll, pokemon = pokemonAll, trainer = trainer, equipos3 = equipos, pokemon3 = pokemon)
    except Exception as ex:
        print(str(ex))
        return redirect(url_for('apptrainer.Error'))

@apptrainer.route('/login',methods=["GET","POST"])
def login_post():
    try:
        if(request.method=="GET"):
            token = request.args.get('token')
            if token:
                info = verificar(token)
                if(info['status']!="fail"):
                    responseObject={
                        'status':"success",
                        'message':'valid token',
                        'info':info
                    }
                    return jsonify(responseObject)
            return render_template('login.html')
        else:
            nombre =request.json['nombre']
            password=request.json['password']
            print(request.json)
            entrenador = Trainer(nombre=nombre,password=password)
            searchTrainer = Trainer.query.filter_by(nombre=nombre).first()
            if searchTrainer:
                validation = bcrypt.check_password_hash(searchTrainer.password,password)
                if validation:
                    auth_token = entrenador.encode_auth_token(user_id=searchTrainer.id)
                    if searchTrainer.admin == True:
                        admin = 1
                    else:
                        admin = 0
                    responseObject={
                        'status':"success",
                        'login':'Loggin exitoso',
                        'auth_token':auth_token,
                        'admin': admin
                    }
                    print(responseObject['admin'])
                    return jsonify(responseObject)
            return jsonify({'message':"Datos incorrectos"})
    except Exception as ex:
        print(str(ex))
        return redirect(url_for('apptrainer.Error'))
    
@apptrainer.route('/sign',methods=["GET","POST"])
def logint_post():
    try:
        if request.method=="GET":
            return render_template('register.html')
        else:
            nombre=request.json['nombre']
            password=request.json['password']
            entrenador = Trainer(nombre=nombre,password=password)
            trainerExists = Trainer.query.filter_by(nombre=nombre).first()
            if not trainerExists:
                try:
                    db.session.add(entrenador)
                    db.session.commit()
                    responseObject={
                        'status':'success',
                        'message':"Registro exitoso"
                    }
                except exc.SQLAlchemyError as e:
                    responseObject={
                        'status':'error',
                        'message':e
                    }
            else:
                responseObject={
                    'status':'error',
                    'message':'entrenador existente'
                }
            return jsonify(responseObject)
    except Exception as ex:
        print(str(ex))
        return redirect(url_for('apptrainer.Error'))
    
@apptrainer.route('/entrenador')
def IndexTrainers():
    try:
        trainers = Trainer.query.order_by("id").all()
        return render_template('indexTrainer.html', trainers = trainers)
    except Exception as ex:
        print(str(ex))
        return redirect(url_for('apptrainer.Error'))

@apptrainer.route('/entrenador/edit/<string:name>', methods = ["GET", "POST"])
def Editar(name):
    try:
        trainer = Trainer.query.filter_by(nombre = name).first()
        formTrainer = TrainerForm(obj = trainer)
        if request.method == "POST":
            if formTrainer.validate_on_submit():
                formTrainer.populate_obj(trainer)
                trainer.encodePassword(trainer.password)          #Encripta la password
                #user.admin = bool(user.admin)               
                if trainer.admin == "True":                    #Convierte la respuesta del RadioButton de String a Booleano
                    trainer.admin = True
                else:
                    trainer.admin = False
                db.session.commit()
                return redirect(url_for('apptrainer.IndexTrainers'))
        else:
            return render_template("editarTrainer.html", editTrainer = formTrainer)
    except Exception as ex:
        print(str(ex))
        return redirect(url_for('apptrainer.Error'))

@apptrainer.route('/entrenador/delete/<int:id>')    
def Eliminar(id):
    try:
        trainer = Trainer.query.filter_by(id = id).first()
        db.session.delete(trainer)
        db.session.commit()
        return redirect(url_for('apptrainer.IndexTrainers'))
    except Exception as ex:
        print(str(ex))
        return redirect(url_for('apptrainer.Error'))
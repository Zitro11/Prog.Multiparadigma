from flask import Blueprint,request,redirect,render_template,url_for
from models import Actor
from forms import ActorForm
from database import db

appactor = Blueprint('appactor',__name__,template_folder='templates')


@appactor.route('/indexActor')
def inicio():
    actores = Actor.query.all()
    return render_template('indexActor.html',actores=actores)


@appactor.route('/agregarActor',methods=["GET","POST"])
def agregar():
    actor = Actor()
    actorForm = ActorForm(obj=actor)
    if request.method=="POST":
        if actorForm.validate_on_submit():
            actorForm.populate_obj(actor)
            db.session.add(actor)
            db.session.commit()
            return redirect(url_for('appactor.inicio'))
    return render_template('agregarActor.html',forma=actorForm)


@appactor.route('/editarActor/<int:id>',methods=["GET","POST"])
def editar(id):
    actor = Actor.query.get_or_404(id)
    actorForm = ActorForm(obj=actor)
    if request.method == "POST":
        if actorForm .validate_on_submit():
            actorForm.populate_obj(actor)
            db.session.commit()
            return redirect(url_for('appactor.inicio'))
    return render_template('editarActor.html',forma=actorForm)


@appactor.route('/eliminarActor/<int:id>')
def eliminar(id):
    actor = Actor.query.get_or_404(id)
    db.session.delete(actor)
    db.session.commit()
    return redirect(url_for('appactor.inicio'))
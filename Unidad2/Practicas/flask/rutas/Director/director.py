from flask import Blueprint,request,redirect,render_template,url_for
from models import Director
from forms import DirectorForm
from database import db

appdirector = Blueprint('appdirector',__name__,template_folder='templates')

@appdirector.route('/indexDirector')
def inicio():
    directores = Director.query.all()
    return render_template('indexDir.html',directores=directores)


@appdirector.route('/agregarDirector',methods=["GET","POST"])
def agregar():
    director = Director()
    directorForm = DirectorForm(obj=director)
    if request.method=="POST":
        if directorForm.validate_on_submit():
            directorForm.populate_obj(director)
            db.session.add(director)
            db.session.commit()
            return redirect(url_for('appdirector.inicio'))
    return render_template('agregarDir.html',forma=directorForm)


@appdirector.route('/editarDirector/<int:id>',methods=["GET","POST"])
def editar(id):
    director = Director.query.get_or_404(id)
    directorForm = DirectorForm(obj=director)
    if request.method == "POST":
        if directorForm .validate_on_submit():
            directorForm.populate_obj(director)
            db.session.commit()
            return redirect(url_for('appdirector.inicio'))
    return render_template('editarDir.html',forma=directorForm)


@appdirector.route('/eliminarDirector/<int:id>')
def eliminar(id):
    director = Director.query.get_or_404(id)
    db.session.delete(director)
    db.session.commit()
    return redirect(url_for('appdirector.inicio'))
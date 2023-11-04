from flask import Blueprint,request,redirect,render_template,url_for
from models import Pelicula
from forms import PeliculaForm
from database import db

appelicula = Blueprint('appelicula',__name__,template_folder='templates')

@appelicula.route('/indexPelicula')
def inicio():
    peliculas = Pelicula.query.all()
    return render_template('indexP.html',peliculas=peliculas)


@appelicula.route('/agregarPelicula',methods=["GET","POST"])
def agregar():
    pelicula = Pelicula()
    peliculaForm = PeliculaForm(obj=pelicula)
    if request.method=="POST":
        if peliculaForm.validate_on_submit():
            peliculaForm.populate_obj(pelicula)
            db.session.add(pelicula)
            db.session.commit()
            return redirect(url_for('appelicula.inicio'))
    return render_template('agregarP.html',forma=peliculaForm)


@appelicula.route('/editarPelicula/<int:id>',methods=["GET","POST"])
def editar(id):
    pelicula = Pelicula.query.get_or_404(id)
    peliculaForm = PeliculaForm(obj=pelicula)
    if request.method == "POST":
        if peliculaForm .validate_on_submit():
            peliculaForm.populate_obj(pelicula)
            db.session.commit()
            return redirect(url_for('appelicula.inicio'))
    return render_template('editarP.html',forma=peliculaForm)


@appelicula.route('/eliminarPelicula/<int:id>')
def eliminar(id):
    pelicula = Pelicula.query.get_or_404(id)
    db.session.delete(pelicula)
    db.session.commit()
    return redirect(url_for('appelicula.inicio'))
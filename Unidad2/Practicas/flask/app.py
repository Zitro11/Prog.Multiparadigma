from flask import Flask, render_template
from database import db
from config import BasicConfig
from flask_migrate import Migrate
import logging

app = Flask(__name__)
app.config.from_object(BasicConfig)
db.init_app(app)
migrate = Migrate(app, db)


from rutas.Actor.actor import appactor
from rutas.Director.director import appdirector
from rutas.Pelicula.pelicula import appelicula
app.register_blueprint(appactor)
app.register_blueprint(appdirector)
app.register_blueprint(appelicula)

logging.basicConfig(level=logging.DEBUG, filename="logs.log")


@app.route('/')
def dashboard():
    return render_template('dashboard.html')



if __name__ == '__main__':
    app.run()
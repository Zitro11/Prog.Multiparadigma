from flask import Flask, flash
from flask_cors import CORS
from database import db
from encriptador import bcrypt
from flask_migrate import Migrate
from config import BaseConfig
from routes.trainer.trainer import apptrainer
from routes.team.team import appteam
from routes.pokemon.pokemon import apppokemon
app=Flask(__name__)
app.register_blueprint(apptrainer)
app.register_blueprint(appteam)
app.register_blueprint(apppokemon)
app.config.from_object(BaseConfig)
CORS(app)
bcrypt.init_app(app)
db.init_app(app)
migrate = Migrate()
migrate.init_app(app,db)


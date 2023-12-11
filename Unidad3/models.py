import jwt
import datetime
from config import BaseConfig
from app import db,bcrypt

class Trainer(db.Model):
    __tablename__="trainer"
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    nombre=db.Column(db.String(255),nullable=False)
    password=db.Column(db.String(255),nullable=False)
    registered_on=db.Column(db.DateTime,nullable=False)
    admin=db.Column(db.Boolean,nullable=False,default=False)

    def __init__(self,nombre,password,admin=False) -> None:
        self.nombre=nombre
        self.password=bcrypt.generate_password_hash(
            password,BaseConfig.BCRYPT_LOG_ROUNDS
        ).decode()

        self.registered_on=datetime.datetime.now()
        self.admin=admin
        
    def encodePassword(self, password):
        self.password = bcrypt.generate_password_hash(password, BaseConfig.BCRYPT_LOG_ROUNDS).decode()

    def encode_auth_token(self,user_id):
        try:
            print('USER',user_id)
            payload={
                'exp':datetime.datetime.utcnow()+datetime.timedelta(hours=5),
                'iat':datetime.datetime.utcnow(),
                'sub':user_id
            }
            print("PAYLOAD",payload)
            return jwt.encode(
                payload,
                BaseConfig.SECRET_KEY,
                algorithm='HS256'
            )
        except Exception as e:
            print("EXCEPTION")
            print(e)
            return e
        
    @staticmethod
    def decode_auth_token(auth_token):
        try:
            payload = jwt.decode(auth_token,BaseConfig.SECRET_KEY,algorithms=['HS256'])
            return payload
        except jwt.ExpiredSignatureError as e:
            return 'Signature Expired Please log in again'

        except jwt.InvalidTokenError as e:
            return 'Invalid token'

class Pokemon(db.Model):
    __tablename__="pokemon"
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    nombre=db.Column(db.String(255),nullable=False)
    tipo=db.Column(db.String(255),nullable=False)
    item=db.Column(db.String(255),nullable=False)
    habilidad=db.Column(db.String(255),nullable=False)
    naturaleza=db.Column(db.String(255),nullable=False)
    sprite_icon=db.Column(db.String(255),nullable=False)
    sprite_front=db.Column(db.String(255),nullable=False)
    movimiento1=db.Column(db.String(255),nullable=False)
    movimiento2=db.Column(db.String(255),nullable=False)
    movimiento3=db.Column(db.String(255),nullable=False)
    movimiento4=db.Column(db.String(255),nullable=False)
    nombre_entrenador=db.Column(db.String(255),nullable=False)

class Team(db.Model):
    __tablename__="team"
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    nombredelequipo=db.Column(db.String(255),nullable=False)
    nombre_entrenador=db.Column(db.String(255),nullable=False)
    id_pokemon1=db.Column(db.Integer,db.ForeignKey('pokemon.id'))
    id_pokemon2=db.Column(db.Integer,db.ForeignKey('pokemon.id'))
    id_pokemon3=db.Column(db.Integer,db.ForeignKey('pokemon.id'))
    id_pokemon4=db.Column(db.Integer,db.ForeignKey('pokemon.id'))
    id_pokemon5=db.Column(db.Integer,db.ForeignKey('pokemon.id'))
    id_pokemon6=db.Column(db.Integer,db.ForeignKey('pokemon.id'))
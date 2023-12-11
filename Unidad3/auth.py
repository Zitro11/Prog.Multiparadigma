from models import Trainer
from functools import wraps
from flask import  jsonify,request


def obtenerInfo(token):
    if token:
        resp = Trainer.decode_auth_token(token)
        print(resp)
        trainer =Trainer.query.filter_by(id=resp['sub']).first()
        if trainer:
            entrenador ={
                'status':'success',
                'data':{
                    'user_id':trainer.id,
                    'nombre':trainer.nombre,
                    'admin':trainer.admin,
                    'registered_on':trainer.registered_on
                }
            }
            return entrenador
        else:
            error ={
                'status':'fail',
                'message':resp
            }
            return error

def tokenCheck(f):
    @wraps(f)
    def verificar(*args,**kwargs):
        token = None
        if 'token' in request.headers:
            token = request.headers['token']
        if not token:
            return jsonify({'message':'Token no encontrado'})
        try:
            info = obtenerInfo(token)
            print(info)
            if info['status']=='fail':
                return jsonify({'message':'Token invalido'})
        except Exception as e:
                print(e)
                return jsonify({'message':"Error"})
        return f(info['data'],*args,**kwargs)
    return verificar

def verificar(token):
        if not token:
            return jsonify({'message':'Token no encontrado'})
        try:
            info = obtenerInfo(token)
            if info['status']=='fail':
                return jsonify({'message':'Token invalido'})
        except Exception as e:
                print(e)
                return jsonify({'message':"Error"})
        return info
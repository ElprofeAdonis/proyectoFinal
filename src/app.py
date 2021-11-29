from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
from sqlalchemy.engine.base import Transaction
from werkzeug.security import generate_password_hash, check_password_hash
import uuid, jwt, datetime
from functools import wraps

from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager, unset_jwt_cookies, set_access_cookies, get_jwt

app = Flask(__name__)

# Setup the Flask-JWT-Extended extension
# app.config["JWT_SECRET_KEY"] = "super-secret-adonis"  # Change this!
# jwt = JWTManager(app)

# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root@localhost/proyecto1"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# db = SQLAlchemy(app)
# api = Api(app)




# app.config["JWT_SECRET_KEY"] = "super-secret-adonis"  # Change this!
# jwt = JWTManager(app)
app.config['SECRET_KEY'] = 'thisisscret'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root@localhost/adonisProyecto5"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
# api = Api(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(60), unique=True)
    name = db.Column(db.String(60))
    password = db.Column(db.String(100))
    admin = db.Column(db.Boolean)


class Info_Parqueo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombreL = db.Column(db.String(200))
    ced_juridica = db.Column(db.String(460))
    duenio = db.Column(db.String(200))
    direccion = db.Column(db.String(3500))
    anio_creacion = db.Column(db.String(80))
    email = db.Column(db.String(360))
    telefono = db.Column(db.String(230))
    cumple_requisitos = db.Column(db.Boolean)
    parqueo_id = db.Column(db.String(190), unique=True)

class Tipo_Espacio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombreC = db.Column(db.String(200))
    descripcion = db.Column(db.String(250))
    placa = db.Column(db.String(90))
    precioPorHora = db.Column(db.Integer)
    espacio_ocupado = db.Column(db.Boolean)
    registro_id = db.Column(db.String(190), unique=True)

class Factura(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    placa = db.Column(db.String(250))
    precioPorHora = db.Column(db.Integer)
    espacio_ocupado = db.Column(db.Boolean)
    registro_id = db.Column(db.String(190), unique=True)




def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'mensaje' : 'Falta el token'}), 401

    

        try:
            data =jwt.decode(token, app.config['SECRET_KEY'])
            current_user =User.query.filter_by(public_id=data['public_id']).first()

        except:
            return jsonify({'mensaje' : 'El Token es invalido'}), 401

        return f(current_user, *args, **kwargs)

    return decorated




@app.route('/user', methods=['GET'])
# @token_required
def get_all_users():

    # if not current_user.admin:
    #     return jsonify({'mensaje' : 'No se puede realizar esta funcion'})


    users = User.query.all()

    output = []

    for user in users:
        user_data = {}
        user_data['public_id'] = user.public_id
        user_data['name'] = user.name
        user_data['password'] = user.password
        user_data['admin'] = user.admin
        output.append(user_data)
    return jsonify({'users' : output})


@app.route('/user/<public_id>', methods=['GET'])
# @token_required
def get_one_user(public_id):

    # if not current_user.admin:
    #     return jsonify({'mensaje' : 'No se puede realizar esta funcion'})


    user = User.query.filter_by(public_id=public_id).first()

    if not user:
        return jsonify({'mensaje' : 'No se encontro ususario'})

    
    user_data = {}
    user_data['public_id'] = user.public_id
    user_data['name'] = user.name
    user_data['password'] = user.password
    user_data['admin'] = user.admin
    
    return jsonify({'user' : user_data})




@app.route('/user', methods=['POST'])
# @token_required
#signup = crear usuario
def signup():

    # if not current_user.admin:
    #     return jsonify({'mensaje' : 'No se puede realizar esta funcion'})

    data = request.get_json()

    hashed_password = generate_password_hash(data['password'], method='sha256')

    new_user =User(public_id=str(uuid.uuid4()), name=data['name'], password=hashed_password, admin=False)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'mensaje' : "Nuevo usuario creado"})



@app.route('/user/<public_id>', methods=['PUT'])
# @token_required
def promote_user(public_id):

    # if not current_user.admin:
    #     return jsonify({'mensaje' : 'No se puede realizar esta funcion'})

    user = User.query.filter_by(public_id=public_id).first()

    if not user:
        return jsonify({'mensaje': 'usuario no encontrado por medio del ID'})

    user.admin = True
    db.session.commit()

    return jsonify({'mensaje' : 'Asido asignado con exto la informacion esperada'})



@app.route('/login')
def login():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response('tines que colocar usuario y password', 401, {'WWW-Authenticate' : 'Basic realm="login required!"'})

    user =User.query.filter_by(name=auth.username).first()

    if not user:
        return make_response('No se puede virificar token', 401, {'WWW-Authenticate' : 'Basic realm="login required!"'})

    if check_password_hash(user.password, auth.password):
        token = jwt.encode({'public_id' : user.public_id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=10000)}, app.config['SECRET_KEY'])

        return jsonify({'token' : token})

    return make_response('No se puede virificar token .', 401, {'WWW-Authenticate' : 'Basic realm="login required!"'})

#************************************************************************************************************************************************************

@app.route('/info_parqueo', methods=['GET'])
# @token_required
def get_all_infoParqueos():

    infoParqueos = Info_Parqueo.query.all()

    output = []

    for infoParqueo in infoParqueos:
        infoParqueo_data ={}
        infoParqueo_data['id']=infoParqueo.id
        infoParqueo_data['nombreL']=infoParqueo.nombreL
        infoParqueo_data['ced_juridica']=infoParqueo.ced_juridica
        infoParqueo_data['duenio']=infoParqueo.duenio
        infoParqueo_data['direccion']=infoParqueo.direccion
        infoParqueo_data['anio_creacion']=infoParqueo.anio_creacion
        infoParqueo_data['email']=infoParqueo.email
        infoParqueo_data['telefono']=infoParqueo.telefono
        infoParqueo_data['cumple_requisitos']=infoParqueo.cumple_requisitos
        infoParqueo_data['parqueo_id']=infoParqueo.parqueo_id
        output.append(infoParqueo_data)

    return jsonify({'infoParqueos' : output})


@app.route('/info_parqueo/<parqueo_id>', methods=['GET'])
# @token_required
def get_one_infoParqueo(parqueo_id):

    infoParqueo = Info_Parqueo.query.filter_by(parqueo_id=parqueo_id).first()

    if not infoParqueo:
        return jsonify({'mensaje' : 'No se encontro informacion de parqueo id'})

    
    infoParqueo_data = {}
    infoParqueo_data['nombreL']=infoParqueo.nombreL
    infoParqueo_data['ced_juridica']=infoParqueo.ced_juridica
    infoParqueo_data['duenio']=infoParqueo.duenio
    infoParqueo_data['direccion']=infoParqueo.direccion
    infoParqueo_data['anio_creacion']=infoParqueo.anio_creacion
    infoParqueo_data['email']=infoParqueo.email
    infoParqueo_data['telefono']=infoParqueo.telefono
    infoParqueo_data['cumple_requisitos']=infoParqueo.cumple_requisitos
    infoParqueo_data['parqueo_id']=infoParqueo.parqueo_id
    
    return jsonify(infoParqueo_data)
    
   

@app.route('/info_parqueo', methods=['POST'])
# @token_required
def create_infoParqueo():


    data =request.get_json()

    new_infoParqueo = Info_Parqueo(nombreL=data['nombreL'], ced_juridica=data['ced_juridica'], duenio=data['duenio'],\
    direccion=data['direccion'], anio_creacion=data['anio_creacion'], email=data['email'], telefono=data['telefono'],\
    cumple_requisitos=False, parqueo_id=str(uuid.uuid4()))
    db.session.add(new_infoParqueo)
    db.session.commit()

    return jsonify({'mensaje' : 'Informacion del parqueo creada'})


@app.route('/info_parqueo/<parqueo_id>', methods=['PUT'])
# @token_required
def promote_infoParqueo(parqueo_id):

    infoParqueo = Info_Parqueo.query.filter_by(parqueo_id=parqueo_id).first()

    if not infoParqueo:
        return jsonify({'mensaje': 'Informacion del parqueo NO asido encontrado'})

    infoParqueo.cumple_requisitos = True
    db.session.commit()

    return jsonify({'mensaje' : 'Requisitos de la informacion asido asignado con exito'})
    return ''
#///////////////////////////////////////////////////////////////////////////////////

@app.route('/tipo_espacio', methods=['GET'])
# @token_required
def get_all_tipoEsapcios():

    tipoEspacios = Tipo_Espacio.query.all()

    output = []

    for tipoEspacio in tipoEspacios:
        infoParqueo_data ={}
        infoParqueo_data['id']=tipoEspacio.id
        infoParqueo_data['nombreC']=tipoEspacio.nombreC
        infoParqueo_data['descripcion']=tipoEspacio.descripcion
        infoParqueo_data['placa']=tipoEspacio.placa
        infoParqueo_data['precioPorHora']=tipoEspacio.precioPorHora
        infoParqueo_data['espacio_ocupado']=tipoEspacio.espacio_ocupado
        infoParqueo_data['registro_id']=tipoEspacio.registro_id
        output.append(infoParqueo_data)

    return jsonify({'tipoEspacios' : output})


@app.route('/tipo_espacio/<registro_id>', methods=['GET'])
# @token_required
def get_one_tipoEspacio(registro_id):

    tipoEspacio = Tipo_Espacio.query.filter_by(registro_id=registro_id).first()

    if not tipoEspacio:
        return jsonify({'mensaje' : 'No se encontro registros del tipo espacio'})

    
    tipoEspacio_data ={}
    tipoEspacio_data['id']=tipoEspacio.id
    tipoEspacio_data['nombreC']=tipoEspacio.nombreC
    tipoEspacio_data['descripcion']=tipoEspacio.descripcion
    tipoEspacio_data['placa']=tipoEspacio.placa
    tipoEspacio_data['precioPorHora']=tipoEspacio.precioPorHora
    tipoEspacio_data['espacio_ocupado']=tipoEspacio.espacio_ocupado
    tipoEspacio_data['registro_id']=tipoEspacio.registro_id
        
    
    return jsonify(tipoEspacio_data)
    
   

@app.route('/tipo_esapcio', methods=['POST'])
# @token_required
def create_tipoEspacio():


    data =request.get_json()

    new_tipoEspacio = Info_Parqueo(nombreC=data['nombreC'], descripcion=data['descripcion'], placa=data['placa'], precioPorHora=data['precioPorHora'], esapcio_ocupado=False, registro_id=str(uuid.uuid4()))
    db.session.add(new_tipoEspacio)
    db.session.commit()

    return jsonify({'mensaje' : 'Informacion de tipo de espacio creada'})


@app.route('/tipo_espacio/<registro_id>', methods=['PUT'])
# @token_required
def promote_tipoEspacio(registro_id):

    infoParqueo = Info_Parqueo.query.filter_by(registro_id=registro_id).first()

    if not infoParqueo:
        return jsonify({'mensaje': 'Registros del espacio no encontrado'})

    infoParqueo.espacio_ocupado = True
    db.session.commit()

    return jsonify({'mensaje' : 'Espacio del parqueo asido asignado aun vehiculo'})

db.create_all()






# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.Text, nullable=False, unique=True)
#     password = db.Column(db.Text, nullable=False)
#     full_name = db.Column(db.Text, nullable=False)

#     # NOTE: In a real application make sure to properly hash and salt passwords
#     def check_password(self, password):
#         return compare_digest(password, "password")


# @jwt.user_identity_loader
# def user_identity_lookup(user):
#     return user.id

# @jwt.user_lookup_loader
# def user_lookup_callback(_jwt_header, jwt_data):
#     identity = jwt_data["sub"]
#     return User.query.filter_by(id=identity).one_or_none()


# @app.route("/login", methods=["POST"])
# def login():
#     username = request.json.get("username", None)
#     password = request.json.get("password", None)

#     user = User.query.filter_by(username=username).one_or_none()
#     if not user:
#         return jsonify("Wrong username or password"), 401

#     # Notice that we are passing in the actual sqlalchemy user object here
#     access_token = create_access_token(identity=user)
#     return jsonify(access_token=access_token)


# @app.route("/who_am_i", methods=["GET"])
# @jwt_required()
# def who_am_i():
#     # We can now access our sqlalchemy User object via `current_user`.
#     return jsonify(
#         id=current_user.id,
#         full_name=current_user.full_name,
#         username=current_user.username,
#     )

# # SignUp
# @app.route("/signup", methods=["POST"])
# def signup():
#     newUser = request.get_json()
#     if (newUser['username'] == "" or newUser['password'] == "" or newUser['full_name'] == ""):
#         return jsonify("Los campos username, passwoed y full name son requeridos."), 401

#     user = User(username=newUser['username'], password=newUser['password'], full_name=newUser['full_name'])
#     db.session.add(user)
#     db.session.commit()
#     return { "response": "Usuario creado exitosamente!"}, 201

# @app.route("/actualizarInfo", methods=["PUT"])
# def actualizarInfo():
#     newUser = User.query.filter_by(id=id).first()
#     datos = request.get_json()
#         # TODO: LOOKUP 'ARGUMENT PARSING for Flask-RESTful'
#     if (datos['username'] == "" or datos['username'] is None or datos['password'] == "" or datos['password'] is None or datos['full_name'] == "" or datos['full_name'] is None):
#             return { "response": "Error al actualizar los datos, User no existe."}, 400

#     newUser.username = datos['username']
#     newUser.password = datos['password']
#     newUser.full_name = datos['full_name']
    # db.session.commit() 

#-----------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------

# @jwt.Parqueo_identity_loader
# def Parqueo_identity_lookup(Parqueo):
#     return Parqueo.id

# @jwt.Parqueo_lookup_loader
# def Parqueo_lookup_callback(_jwt_header, jwt_data):
#     identity = jwt_data["sub"]
#     return Parqueo.query.filter_by(id=identity).one_or_none()

# class Parqueo(db.Model):
#     id = db.Column(db.INteger, prymary_key=True)
#     username = db.Column(db.String(250), nullablle=False, unique=True)
#     cedula_juridica = db.Column(db.String(250), nullablle=False, unique=True)
#     duenio = db.Column(db.String(100), nullablle=False, unique=True)
#     direccion = db.Column(db.String(300), nullablle=False, unique=True)
#     anio_creacion = db.Column(db.String(100), nullablle=False, unique=True)
#     direccion_correo = db.Column(db.String(300), nullablle=False, unique=True)
#     telefono = db.Column(db.String(100), nullablle=False, unique=True)

#     def __repr__(self):
#         return "<Estacionamiento %r>" % self.username
    
#     def serialize(self):
#         return {
#             "username": self.username,
#             "cedula_juridica": self.cedula_juridica,
#             "duenio": self.duenio,
#             "direccion": self.direccion_correo,
#             "anio_creacion": self.anio_creacion,
#             "direccion_correo": self.direccion_correo,
#             "telefono": self.telefono
#         }

# class IndexRoute(Resource):
#     def get(self):
#         return{"response": "hola, este es el index route del parqueo"}

# class IndexEstacionamiento(Resource):
#     def get(self):
#         info_Parqueo = Parqueo.query.all()
#         response = []
#         if info_Parqueo:
#             for estacionamiento in info_Parqueo:
#                 response.append(
#                     {
#                         "id": estacionamiento.id,
#                         "username": estacionamiento.username,
#                         "cedula_juridica": estacionamiento.cedula_juridica,
#                         "duenio": estacionamiento.duenio,
#                         "direccion": estacionamiento.direccion,
#                         "anio_creacion": estacionamiento.anio_creacion,
#                         "direccion_correo": estacionamiento.direccion_correo,
#                         "telefono": estacionamiento.telefono,
#                     }
#                 )

#         return {"response": response}, 200

#     def post(self):
#         estacionamientoACrear = request.get_json()
#         if (estacionamientoACrear['username'] == "" or estacionamientoACrear['cedula_juridica'] == "" or estacionamientoACrear['duenio'] == "" \
#             or estacionamientoACrear['direccion'] == "" or estacionamientoACrear['anio_creacion'] == "") or estacionamientoACrear['direccion_correo'] == "" \
#                 or estacionamientoACrear['telefono'] == "":
#             return { "response": "Error al ingregar los datos, revise que todos los campos requeridos tengan informacion"}, 400
#         estacionamiento = Parqueo(username=estacionamientoACrear['username'], cedula_juridica=estacionamientoACrear['cedula_juridica'],\
#              duenio=estacionamientoACrear['duenio'], direccion=estacionamientoACrear['direccion'], anio_creacion=estacionamientoACrear['anio_creacion'],\
#                  direccion_correo=estacionamientoACrear['direccion_correo'], telefono=estacionamientoACrear['telefono'])
#         db.session.add(estacionamiento)
#         db.session.commit()
#         return { "response": " Estacionamiento creado exitosamente!"}, 201

# class UserById(Resource):
#     def get(self, id):
#         estacionamiento = Parqueo.query.filter_by(id=id).first()

#         if (estacionamiento is None):
#             return { "response": "Error al obtener los datos, el pokemon no existe."}, 400
 
#         return {'response': {
#             "id": estacionamiento.id,
#             "username": estacionamiento.username,
#             "cedula_juridica": estacionamiento.cedula_juridica,
#             "duenio": estacionamiento.duenio,
#             "direccion": estacionamiento.direccion,
#             "anio_creacion": estacionamiento.anio_creacion,
#             "direccion_correo": estacionamiento.direccion_correo,
#             "telefono": estacionamiento.telefono,
#         }}, 200

#     def put(self, id):
#         estacionamiento = Parqueo.query.filter_by(id=id).first()
#         datos = request.get_json()
#         # TODO: LOOKUP 'ARGUMENT PARSING for Flask-RESTful'
#         if (datos['username'] == "" or datos['username'] is None or datos['cedula_juridica'] == "" or datos['cedula_juridica'] is None \
#             or datos['duenio'] == "" or datos['duenio'] is None or datos['direccion'] == "" or datos['direccion'] is None or datos['anio_creacion'] == "" or datos['anio_creacion'] is None \
#                 or datos['direccion_correo'] == "" or datos['direccion_correo'] is None or datos['telefono'] == "" or datos['telefono'] is None):
#             return { "response": "Error al actualizar los datos, info_parqueo no existe."}, 400

#         estacionamiento.username = datos['username']
#         estacionamiento.cedula_juridica = datos['cedula_juridica']
#         estacionamiento.duenio = datos['duenio']
#         estacionamiento.direccion = datos['direccion']
#         estacionamiento.anio_creacion = datos['anio_creacion']
#         estacionamiento.direccion_correo = datos['direccion_correo']
#         estacionamiento.telefono = datos['telefono']
#         db.session.commit()
 
#         return {"response": "INformacion del parqueo actualizado con exito!"}

#     def delete(self, id):
#         estacionamiento = Parqueo.query.filter_by(id=id).first()

#         if (estacionamiento is None):
#             return { "response": "Error al borrar los datos, el de la informacio de parqueo no existe."}, 400

#         db.session.delete(estacionamiento)
#         db.session.commit()
#         return { "response": "Anime con id: {anime}. Borrado exitosamente. ".format(anime=id)}, 203


# @app.route("/login1", methods=["POST"])
# def login():
#     username = request.json.get("username", None)
#     cedula_juridica = request.json.get("cedula_juridica", None)
#     duenio = request.json.get("duenio", None)
#     direccion = request.json.get("direccion", None)
#     anio_creacion = request.json.get("anio_creacion", None)
#     direccion_correo = request.json.get("direccion_correo", None)
#     telefono = request.json.get("telefono", None)
    

#     Parqueo = Parqueo.query.filter_by(username=username).one_or_none()
#     if not Parqueo:
#         return jsonify("Wrong username or password"), 401

#     # Notice that we are passing in the actual sqlalchemy user object here
#     access_token = create_access_token(identity=Parqueo)
#     return jsonify(access_token=access_token)

#-----------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------
     

# @app.after_request
# def refresh_expiring_jwts(response):
#     try:
#         exp_timestamp = get_jwt()["exp"]
#         now = datetime.now(timezone.utc)
#         target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
#         if target_timestamp > exp_timestamp:
#             access_token = create_access_token(identity=get_jwt_identity())
#             set_access_cookies(response, access_token)
#         return response
#     except (RuntimeError, KeyError):
#         # Case where there is not a valid JWT. Just return the original respone
#         return response



# @app.route("/logout", methods=["POST"])
# # cerrar secion...
# def logout():
#     response = jsonify({"msg": "logout successful"})
#     unset_jwt_cookies(response)
#     return response

# db.create_all()
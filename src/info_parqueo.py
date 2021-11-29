# from flask_sqlalchemy import SQLAlchemy
# from flask_restful import Resource, Api
# from flask import Flask, app, request, jsonify

# from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager, current_user, unset_jwt_cookies, set_access_cookies, get_jwt


# db = SQLAlchemy()
# api =Api(app)

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

# # @jwt.Parqueo_identity_loader
# # def Parqueo_identity_lookup(Parqueo):
# #     return Parqueo.id

# # @jwt.Parqueo_lookup_loader
# # def Parqueo_lookup_callback(_jwt_header, jwt_data):
# #     identity = jwt_data["sub"]
# #     return Parqueo.query.filter_by(id=identity).one_or_none()

# class IndexRoute(Resource):
#     def get(self):
#         return{"response": "hola, este es el index route del parqueo"}

# @app.route("/signup/info_Parqueo", methods=["POST"])
# def signup():
#     estacionamientoACrear = request.get_json()
#     if (estacionamientoACrear['username'] == "" or estacionamientoACrear['cedula_juridica'] == "" or estacionamientoACrear['duenio'] == "" \
#         or estacionamientoACrear['direccion'] == "" or estacionamientoACrear['anio_creacion'] == "") or estacionamientoACrear['direccion_correo'] == "" \
#             or estacionamientoACrear['telefono'] == "":
#         return { "response": "Error al ingregar los datos, revise que todos los campos requeridos tengan informacion"}, 400
#     estacionamiento = Parqueo(username=estacionamientoACrear['username'], cedula_juridica=estacionamientoACrear['cedula_juridica'],\
#         duenio=estacionamientoACrear['duenio'], direccion=estacionamientoACrear['direccion'], anio_creacion=estacionamientoACrear['anio_creacion'],\
#             direccion_correo=estacionamientoACrear['direccion_correo'], telefono=estacionamientoACrear['telefono'])
#     db.session.add(estacionamiento)
#     db.session.commit()
#     return { "response": " Estacionamiento creado exitosamente!"}, 201

# @app.route("/who_am_i", methods=["GET"])
# @jwt_required()
# def who_am_i():
#     # We can now access our sqlalchemy User object via `current_user`.
#     return jsonify(
#         id=current_user.id,
#         username=current_user.username,
#         cedula_juridica=current_user.cedulu_juridica,
#         duenio=current_user.duenio,
#         direccion=current_user.direccion,
#         anio_creacion=current_user.anio_creacion,
#         direccion_correo=current_user.direccion_correo,
#         telefono=current_user.telefono,
#     )

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


# db.create_all()

# #----------------------------
# #----------------------------
# # GET
# api.add_resource(IndexRoute, '/')
# # GET, POST
# api.add_resource(IndexEstacionamiento, '/info_Parqueo')
# # GET, PUT, DELETE
# api.add_resource(UserById, '/info_Parqueo/<int:id>')
from flask import Blueprint, jsonify, request, make_response
from models.sizes_model import SizesModel
from utils.db import db

add_size = Blueprint("size_BP", __name__)

# Función de inicialización para cargar datos en la base de datos
def init_db():
    # Verifica si ya existen datos en la tabla Producto
    if not SizesModel.query.first():
        # Si no hay datos, carga los datos iniciales
        sizes = [
            SizesModel(size = ["S", "M", "L", "X", "XL", "XXL"]),
            SizesModel(size = ["SS","S", "M", "L", "X", "XL", "XXL", "XXXL"]),
        ]
        db.session.bulk_save_objects(sizes)
        db.session.commit()

# Llamada a la función de inicialización al iniciar la aplicación
@add_size.before_request
def before_request():
    init_db()

@add_size.route("/", methods = ["POST"])
def set_size():
    data = request.get_json()
    size = data.get("size")

    size = SizesModel(size=size)

    db.session.add(size)
    db.session.commit()

    #custom request json
    request_json = jsonify({"status": "success",
                            "message": "Datos guardados correctamente",
                            "data": data})

    #custom request header
    request_make = make_response(request_json)
    request_make.headers['Header'] = 'HTTP/1.1 200 Created'
    request_make.headers['location'] = '/'

    return request_make

@add_size.route("/", methods = ["GET"])
def get_size():
    size = SizesModel.query.all()
    results = [
        {
            "id": sizes.id,
            "size": sizes.size,
        } for sizes in size
        
    ]
    
    return jsonify({"data": results})
from flask import Blueprint, jsonify, request, make_response
from models.sizes_model import SizesModel
from utils.db import db

add_size = Blueprint("size_BP", __name__)

@add_size.route("/", methods = ["POST"])
def set_size():
    data = request.get_json()
    name = data.get("name")
    state = data.get("state")

    size = SizesModel(name=name, state=state)

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
            "id": size.id,
            "name": size.name,
            "state": size.state
        } for size in size
        
    ]
    
    return jsonify({"data": results})
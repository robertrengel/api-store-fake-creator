from flask import Blueprint, jsonify, request, make_response
from models.colors_model import ColorsModel
from utils.db import db

add_color = Blueprint("color_BP", __name__)

@add_color.route("/", methods = ["POST"])
def set_color():
    data = request.get_json()
    color = data.get("color")
    
    available_colors = ColorsModel(color = color)
    
    db.session.add(available_colors)
    db.session.commit()
    
    #custom request json
    request_json = jsonify({"status":"request success",
                            "message":"Data guardados correctamente",
                            "data":data})
    
    #custom request header
    request_make = make_response(request_json)
    request_make.headers['Header'] = 'HTTP/1.1 200 Created'
    request_make.headers['location'] = '/'
    
    return request_make

@add_color.route("/", methods = ["GET"])
def get_color():
    available_colors = ColorsModel.query.all()
    results = [
        {
            "id": available_color.id,
            "color": available_color.color
        } for available_color in available_colors
        
    ]
    return jsonify({"data": results})
    
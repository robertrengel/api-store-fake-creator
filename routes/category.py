from flask import Blueprint, jsonify, request, make_response
from models.prueba import Prueba
from utils.db import db

add_user = Blueprint("category_BP", __name__)


@add_user.route("/", methods  = ["POST"])
def set_category():
    data = request.get_json()
    fullname = data.get("fullname")
    email  = data.get("email")
    phone = data.get("phone")
    
    prueba = Prueba(fullname=fullname, email=email,phone=phone)
    
    db.session.add(prueba)
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

@add_user.route("/", methods = ["GET"])
def get_category():
    category = Prueba.query.all()
    results = [
            {
                "id":categorys.id,
                "fullname": categorys.fullname,
                "email": categorys.email,
                "phone": categorys.phone
            } for categorys in category]
    

    return jsonify({"category": results})


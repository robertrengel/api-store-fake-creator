from flask import Blueprint, jsonify, request, make_response
from models.brand_model import BrandModel
from utils.db import db

add_brand = Blueprint("brand_BP", __name__)

@add_brand.route("/", methods = ["GET"])
def get_brands():
    brands = BrandModel.query.all()
    results = [
        {
            "id": brands.id,
            "name": brands.name,
            "country": brands.country
        } for brands in brands
    ]
    return jsonify({"brands": results})

@add_brand.route("/", methods = ["POST"])
def set_brand():
    data = request.get_json()
    name = data.get("name")
    country = data.get("country")
    
    brand = BrandModel(name=name, country=country)
    
    db.session.add(brand)
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
from flask import Blueprint, jsonify, request, make_response
from models.brand_model import BrandModel
from utils.db import db

add_brand = Blueprint("brand_BP", __name__)

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

@add_brand.route("/<int:brand_id>", methods=["GET"])
def get_brand_by_id(brand_id):
    brand = BrandModel.query.get(brand_id)
    if not brand:
        return jsonify({"message": "Brand not found"}), 404
    return jsonify({
        "id": brand.id,
        "name": brand.name,
        "country": brand.country
    })

@add_brand.route("/<int:brand_id>", methods=["PUT"])
def update_brand(brand_id):
    brand = BrandModel.query.get(brand_id)
    if not brand:
        return jsonify({"message": "Brand not found"}), 404
    
    data = request.get_json()
    name = data.get("name", brand.name)
    country = data.get("country", brand.country)
    
    brand.name = name
    brand.country = country
    
    db.session.commit()
    
    return jsonify({
        "id": brand.id,
        "name": brand.name,
        "country": brand.country
    }), 200

@add_brand.route("/<int:brand_id>", methods=["DELETE"])
def delete_brand(brand_id):
    brand = BrandModel.query.get(brand_id)
    if not brand:
        return jsonify({"message": "Brand not found"}), 404

    db.session.delete(brand)
    db.session.commit()

    return jsonify({"message": "Brand deleted successfully"}), 200

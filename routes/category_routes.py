from flask import Blueprint, jsonify, request, make_response
from models.category_model import CategoryModel
from utils.db import db

add_category = Blueprint("categories_BP", __name__)

@add_category.route("/",methods = ["POST"])
def set_category():
    data = request.get_json()
    categories = data.get("categories")

    category = CategoryModel(categories=categories)

    db.session.add(category)
    db.session.commit()

    #custom request json
    request_json = jsonify({"status": "success",
                            "message": "Data guardados correctamente",
                            "data": data})

    #custom request header
    request_make = make_response(request_json)
    request_make.headers['Header'] = 'HTTP/1.1 200 Created'
    request_make.headers['location'] = '/'

    return request_make

@add_category.route("/",methods = ["GET"])
def get_category():
    category = CategoryModel.query.all()
    results = [
        {
            "id": categorys.id,
            "categories": categorys.category
        } for categorys in category
    ]

    return jsonify({"category": results})
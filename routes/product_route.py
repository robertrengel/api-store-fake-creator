from flask import Blueprint, jsonify, request, make_response
from models.product_model import ProductModel
from utils.db import db

add_product = Blueprint("product_BP", __name__)

@add_product.route("/", methods  = ["POST"])
def set_product():
    data = request.get_json()
    name = data.get("name")
    description = data.get("description")
    image = data.get("image")
    price = data.get("price")
    discount = data.get("discount")
    rating = data.get("rating")
    review = data.get("review")
    stock = data.get("stock")
    sales_count = data.get("sales_count")
    create_at = data.get("create_at")
    brand_id = data.get("brand_id")
    
    product = ProductModel(name = name,
                           description = description,
                           image = image,
                           price = price,
                           discount = discount,
                           rating = rating,
                           review = review,
                           stock = stock,
                           sales_count = sales_count,
                           create_at = create_at,
                           brand_id = brand_id)
    
    db.session.add(product)
    db.session.commit()
    
    request_json = jsonify({"status": "success",
                            "message": "Data guardados correctamente",
                            "data": data})
    
    request_make = make_response(request_json)
    request_make.headers['Header'] = 'HTTP/1.1 200 Created'
    request_make.headers['location'] = '/'
    
    return request_make

@add_product.route("/", methods  = ["GET"])
def get_product():
    product = ProductModel.query.all()
    results = [
            {
                "id":products.id,
                "name": products.name,
                "description": products.description,
                "image": products.image,
                "price": products.price,
                "discount": products.discount,
                "rating": products.rating,
                "review": products.review,
                "stock": products.stock,
                "sales_count": products.sales_count,
                "create_at": products.create_at,
                "brand_id": products.brand_id
            } for products in product
    ]
    return jsonify({"products": results})
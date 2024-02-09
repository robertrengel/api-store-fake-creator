from flask import Blueprint, jsonify, request, make_response
from models import ProductModel
from utils.db import db

join = [db.joinedload(ProductModel.brand),
        db.joinedload(ProductModel.available_sizes),
        db.joinedload(ProductModel.available_colors),
        db.joinedload(ProductModel.tag)]

add_product = Blueprint("product_BP", __name__)

@add_product.route("/", methods  = ["POST"])
def set_product():
    data = request.get_json()
    name = data.get("name")
    description = data.get("description")
    image = data.get("image")
    images = data.get("images")
    price = data.get("price")
    discount = data.get("discount")
    rating = data.get("rating")
    review = data.get("review")
    stock = data.get("stock")
    sales_count = data.get("sales_count")
    create_at = data.get("create_at")
    brand_id = data.get("brand_id")
    tag_id = data.get("tag_id")
    available_sizes_id = data.get("available_sizes_id")
    available_color_id = data.get("available_color_id")
    categories_id = data.get("categories_id")
    
    product = ProductModel(name = name,
                           description = description,
                           image = image,
                           images = images,
                           price = price,
                           discount = discount,
                           rating = rating,
                           review = review,
                           stock = stock,
                           sales_count = sales_count,
                           create_at = create_at,
                           brand_id = brand_id,
                           tag_id = tag_id,
                           available_sizes_id= available_sizes_id,
                           available_color_id= available_color_id,
                           categories_id= categories_id
                           )
                            
    
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
    product = ProductModel.query.options(join).all()
    print("aqui algo que se imprime", product[0].images)
    results = [
            {
                "id":products.id,
                "name": products.name,
                "description": products.description,
                "image": products.image,
                "images": products.images,
                "price": products.price,
                "discount": products.discount,
                "rating": products.rating,
                "review": products.review,
                "stock": products.stock,
                "sales_count": products.sales_count,
                "create_at": products.create_at,
                "brand": {
                    "id": products.brand.id,
                    "name": products.brand.name       
                },
                "tags":{
                    "id": products.tag.id,
                    "tag": products.tag.label
                },
                "sizes":{
                    "id": products.available_sizes.id,
                    "sizes": products.available_sizes.size
                },
                "colors": {
                    "id": products.available_color.id,
                    "colors": products.available_color.color
                },
                "categories":{
                    "id": products.categories.id,
                    "categories": products.categories.categories
                    
                }
                
            } for products in product
    ]
    return jsonify({"products": results})

# ! hay problemas con el get. no se detectan el ide del color
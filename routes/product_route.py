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
    seller_id = data.get("seller_id")
    
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
                           categories_id= categories_id,
                           seller_id= seller_id
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
    products = ProductModel.query.options(join).all()
    print("aqui algo que se imprime", products[0].images)
    results = [
            {
                "id":product.id,
                "name": product.name,
                "description": product.description,
                "image": product.image,
                "images": product.images,
                "price": product.price,
                "discount": product.discount,
                "rating": product.rating,
                "review": product.review,
                "stock": product.stock,
                "sales_count": product.sales_count,
                "create_at": product.create_at,
                "brand": {
                    "id": product.brand.id,
                    "name": product.brand.name       
                },
                "tags":{
                    "id": product.tag.id,
                    "tag": product.tag.label
                },
                "sizes":{
                    "id": product.available_sizes.id,
                    "sizes": product.available_sizes.size
                },
                "colors": {
                    "id": product.available_colors.id,
                    "colors": product.available_colors.color
                },
                "categories":{
                    "id": product.categories.id,
                    "categories": product.categories.categories
                    
                },
                "seller":{
                    "id": product.seller.id,
                    "name": product.seller.name,
                    "store_id": product.seller.store_number,
                    "state": product.seller.state
                    
                }
                
            } for product in products
    ]
    return jsonify({"products": results})


#! verificar porque la relaciones de las tablas intermendis aunque se 
#! estan creando no hay ningun valor en ellas.
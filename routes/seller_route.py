from flask import Blueprint, jsonify, request, make_response
from models.seller_model import SellerModel
from utils.db import db

add_seller = Blueprint("seller_BP", __name__)

@add_seller.route("/", methods = ["POST"])
def set_seller():
    data = request.get_json()
    name = data.get("name")
    store_number = data.get("store_number")
    state = data.get("state")

    seller = SellerModel(name=name, store_number=store_number, state=state)

    db.session.add(seller)
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

@add_seller.route("/", methods = ["GET"])
def get_seller():
    seller = SellerModel.query.all()
    results = [
        {
            "id": seller.id,
            "name": seller.name,
            "store_id": seller.store_number,
            "state": seller.state
        } for seller in seller
    ]

    return jsonify({"data": results})
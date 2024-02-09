from flask import Blueprint,jsonify, request, make_response
from models.tag_model import TagModel
from utils.db import db

add_tag = Blueprint("tag_BP", __name__)

def init_db():
    if not TagModel.query.first():
        tags = [
            TagModel(label = ["Electronic", "shift", "Toys"]),
            TagModel(label= ["Home","Children"])
        ]
        db.session.bulk_save_objects(tags)
        db.session.commit()

@add_tag.before_request
def before_request():
    init_db()

@add_tag.route("/", methods = ["POST"])
def set_tag():
    data = request.get_json()
    label = data.get("tag")
    
    tag = TagModel(label= label)
    
    db.session.add(tag)
    db.session.commit()
    
    request_jon = jsonify({"status": "success",
                          "message": "Datos guardados correctamente",
                          "data": data})
    
    request_make = make_response(request_jon)
    request_make.headers['Header'] = 'HTTP/1.1 200 Created'
    request_make.headers['location'] = '/'
    
    return request_make

@add_tag.route("/", methods = ["GET"])
def get_tag():
    tag = TagModel.query.all()
    results = [
        {
            "id": tags.id,
            "tag": tags.label
        } for tags in tag
    ]
    
    return jsonify({"tag": results})
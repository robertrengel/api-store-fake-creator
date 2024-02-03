from flask import Flask
from database.db_config import Dd_Configuration
from utils.error_404 import page_not_found
from utils.db import db

# import routes
from routes import category,index,product_route as product, brand_route as brand

app = Flask(__name__)

#database Connection
app.config.from_object(Dd_Configuration)
db.init_app(app)

#import models
from models.prueba import Prueba
from models.product_model import ProductModel
from models.brand_model import BrandModel

# Blueprint
app.register_blueprint(index.main_bp)
app.register_blueprint(category.add_user, url_prefix="/category")
app.register_blueprint(product.add_product, url_prefix="/product")
app.register_blueprint(brand.add_brand, url_prefix="/brand")

# error handlers
app.register_error_handler(404, page_not_found)


# @app.route('/')
# def hello():
#     return '¡Hola, mundo! Esta es mi API.'


# ver como se elimina la creacion de la tabla alambique en la base de datos
# ver como se inicializa la creacion de la carpeta migracion desde una funcion aparte

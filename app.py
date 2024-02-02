from flask import Flask
from database.db_config import Dd_Configuration
from utils.error_404 import page_not_found
from utils.db import db

# import routes
from routes import category, index

app = Flask(__name__)

#database Connection
app.config.from_object(Dd_Configuration)
db.init_app(app)

#import models
from models.prueba import Prueba

# Blueprint
app.register_blueprint(index.main_bp)
app.register_blueprint(category.add_user, url_prefix="/category")

# error handlers
app.register_error_handler(404, page_not_found)


# @app.route('/')
# def hello():
#     return '¡Hola, mundo! Esta es mi API.'


# ver como se elimina la creacion de la tabla alambique en la base de datos
# ver como se inicializa la creacion de la carpeta migracion desde una funcion aparte

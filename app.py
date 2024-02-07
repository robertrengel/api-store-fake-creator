from flask import Flask
from database.db_config import Dd_Configuration
from utils.error_404 import page_not_found
from utils.db import db

# import routes
from routes import(index,
                   product_route as product,
                   brand_route as brand,
                   category_routes as categories,
                   color_routes as color,
                   tag_route as tag,
                   seller_route as seller,
                   sizes_route as size)

app = Flask(__name__)

#database Connection
app.config.from_object(Dd_Configuration)

#init app
db.init_app(app)

#import models
from models import (SizesModel,
                    TagModel,
                    ColorsModel,
                    CategoryModel,
                    SellerModel,
                    ProductModel,
                    BrandModel,
                )

@db.event.listens_for(db.metadata, "after_create")
def after_create_all(target, connection, **kw):
    if db.session.query(db.func.count(SizesModel.size)).scalar() == 0:
        sizes = SizesModel(size=["XS", "S", "M", "L", "XL", "XXL"])
        db.session.add(sizes)
        db.session.commit()
        print("se añadieron los datos a la tabla sizes")
    else:
        print("la tabla sizes ya tiene datos")
    
    if db.session.query(db.func.count(TagModel.label)).scalar() == 0:
        labels = TagModel(label=["electronic", "shit","cosmetic","food"])
        db.session.add(labels)
        db.session.commit()
        print("se añadieron los datos a la tabla tags")
    else:
        print("la tabla tags ya tiene datos")
    
    if db.session.query(db.func.count(ColorsModel.color)).scalar() == 0:
        colors = ColorsModel(color=["red", "blue", "green", "black", "white"])
        db.session.add(colors)
        db.session.commit()
        print("se añadieron los datos a la tabla colors")
    else:
        print("la tabla colors ya tiene datos")

   # ! este codigo funciona siempre que la tabla esta creada
   # --> hay que colocar la creacion de las tablas en un lugar mas apsesible

# Blueprint
app.register_blueprint(index.main_bp)
app.register_blueprint(product.add_product, url_prefix="/product")
app.register_blueprint(brand.add_brand, url_prefix="/brand")
app.register_blueprint(categories.add_category, url_prefix="/categories")
app.register_blueprint(color.add_color, url_prefix="/color")
app.register_blueprint(tag.add_tag, url_prefix="/tag")
app.register_blueprint(seller.add_seller, url_prefix="/seller")
app.register_blueprint(size.add_size, url_prefix="/size")


# error handlers
app.register_error_handler(404, page_not_found)
from flask import Flask
from database.db_config import Dd_Configuration
from utils.error_404 import page_not_found
from utils.db import db

#import models
from models import (SizesModel,
                    TagModel,
                    ColorsModel,
                    CategoryModel,
                    SellerModel,
                    ProductModel,
                    BrandModel,
                )
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
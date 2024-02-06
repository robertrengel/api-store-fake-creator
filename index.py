from app import app, db
from models.brand_model import BrandModel
from models.category_model import CategoryModel
from models.colors_model import ColorsModel
from models.tag_model import TagModel
from models.sizes_model import SizesModel
from models.product_model import ProductModel

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run()

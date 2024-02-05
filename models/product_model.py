from utils.db import db
from .enum.sizes_enum import Sizes
from .enum.color_enum import Colors


class ProductModel(db.Model):
    __tablename__ = "product"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.Text)
    image = db.Column(db.String(255))
    images = db.Column(db.ARRAY(db.String(255)))
    price = db.Column(db.Float)
    discount = db.Column(db.Float)
    rating = db.Column(db.Float)
    review = db.Column(db.Integer)
    available_sizes = db.Column(db.Enum(Sizes))
    available_colors = db.Column(db.Enum(Colors))
    stock = db.Column(db.Integer)
    sales_count = db.Column(db.Integer)
    create_at = db.Column(db.DateTime)
    tags = db.Column(db.ARRAY(db.String(255)))
    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    brand = db.relationship('BrandModel', back_populates='products')
    categories = db.relationship('CategoryModel', back_populates='products')
    
    def __init__(self, name, description, image, price, discount, rating, review, stock, sales_count, create_at, brand_id):
        self.name = name
        self.description = description
        self.image = image
        self.price = price
        self.discount = discount
        self.rating = rating
        self.review = review
        self.stock = stock
        self.sales_count = sales_count
        self.create_at = create_at
        self.brand_id = brand_id
        

# --> hay que definir los nuevos valores de las rutas
# # !hay que probar que funcione los enum
# * todas las tabla parecen estar bien creadas
from utils.db import db

class ProductModel(db.Model):
    __tablename__ = "product"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.Text)
    image = db.Column(db.String(255))
    price = db.Column(db.Float)
    discount = db.Column(db.Float)
    rating = db.Column(db.Float)
    review = db.Column(db.Integer)
    stock = db.Column(db.Integer)
    sales_count = db.Column(db.Integer)
    create_at = db.Column(db.DateTime)
    
    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'))
    # brand = db.relationship('BrandModel', back_populates='products')
    
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
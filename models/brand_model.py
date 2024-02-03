from utils.db import db

class BrandModel(db.Model):
    __tablename__ = "brand"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    country = db.Column(db.String(255))
    
    products = db.relationship('ProductModel', backref='brand', lazy=True)

    def __init__(self, name, country):
        self.name = name
        self.country = country
        
        
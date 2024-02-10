from utils.db import db

class SellerModel(db.Model):
    __tablename__ = "seller"
    
    id = db.Column(db.Integer, primary_key =True)
    name = db.Column(db.String(255))
    store_number = db.Column(db.String(10))
    state = db.Column(db.String(10))
    
    products = db.relationship("ProductModel", back_populates = "seller")
    
    def __init__(self, name, store_number, state):
        self.name = name
        self.store_number = store_number
        self.state = state

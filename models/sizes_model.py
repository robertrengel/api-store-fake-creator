from utils.db import db

class SizesModel(db.Model):
    __tablename__ = "available_sizes"
    
    id = db.Column(db.Integer, primary_key = True)
    size = db.Column(db.ARRAY(db.String(50)))
    products = db.relationship("ProductModel", back_populates = "available_sizes")
    
    def __init__(self, size):
        self.size = size

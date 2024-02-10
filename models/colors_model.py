from utils.db import db

class ColorsModel(db.Model):
    __tablename__ = "available_colors"
    
    id = db.Column(db.Integer, primary_key = True)
    color = db.Column(db.ARRAY(db.String(50)))
    products = db.relationship("ProductModel", back_populates = "available_colors")
    def __init__(self, color):
        self.color = color
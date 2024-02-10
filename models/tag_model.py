from utils.db import db

class TagModel(db.Model):
    __tablename__ = "tag"
    
    id = db.Column(db.Integer, primary_key = True)
    label = db.Column(db.ARRAY(db.String(50)))
    products = db.relationship("ProductModel", back_populates = "tag")
    
    def __init__(self, label):
        self.label = label
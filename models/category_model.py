from utils.db import db

class CategoryModel(db.Model):
    __tablename__ = "categories"
    
    id = db.Column(db.Integer, primary_key = True)
    categories = db.Column(db.String(100))
    products = db.relationship('ProductModel', back_populates = 'categories', lazy = True)    
    
    def __ini__(self,categories):
        self.categories = categories
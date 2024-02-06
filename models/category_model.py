from utils.db import db

categories_products = db.Table('categories_products',
    db.Column('categories_id', db.Integer, db.ForeignKey('categories.id'), primary_key=True),
    db.Column('product_id', db.Integer, db.ForeignKey('product.id'), primary_key=True)
)

class CategoryModel(db.Model):
    __tablename__ = "categories"
    
    id = db.Column(db.Integer, primary_key = True)
    categories = db.Column(db.String(100))
    products = db.relationship('ProductModel', secondary = categories_products, back_populates = 'categories')    
    
    def __ini__(self,categories):
        self.categories = categories
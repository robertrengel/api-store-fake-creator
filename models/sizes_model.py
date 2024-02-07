from utils.db import db

size_product = db.Table("size_product",
    db.Column("size_id", db.Integer, db.ForeignKey("available_sizes.id"), primary_key = True),
    db.Column("product_id", db.Integer, db.ForeignKey("product.id"), primary_key = True)
)

class SizesModel(db.Model):
    __tablename__ = "available_sizes"
    
    id = db.Column(db.Integer, primary_key = True)
    size = db.Column(db.ARRAY(db.String(50)))
    products = db.relationship("ProductModel", secondary = size_product, back_populates = "available_sizes")
    
    def __init__(self, size):
        self.size = size

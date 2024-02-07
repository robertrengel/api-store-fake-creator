from utils.db import db

tag_product = db.Table("tag_product",
    db.Column("tag_id", db.Integer, db.ForeignKey("tag.id"), primary_key = True),
    db.Column("product_id", db.Integer, db.ForeignKey("product.id"), primary_key = True)
)

class TagModel(db.Model):
    __tablename__ = "tag"
    
    id = db.Column(db.Integer, primary_key = True)
    label = db.Column(db.ARRAY(db.String(50)))
    products = db.relationship("ProductModel", secondary = tag_product, back_populates = "tag")
    
    def __init__(self, label):
        self.label = label
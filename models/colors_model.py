from utils.db import db

color_product = db.Table("color_product",
    db.Column("color_id",db.Integer, db.ForeignKey("available_colors.id"),primary_key = True),
    db.Column("product_id",db.Integer, db.ForeignKey("product.id"), primary_key = True)
)

class ColorsModel(db.Model):
    __tablename__ = "available_colors"
    
    id = db.Column(db.Integer, primary_key = True)
    color = db.Column(db.ARRAY(db.String(50)))
    products = db.relationship("ProductModel", secondary = color_product, back_populates = "available_colors")
    def __init__(self, color):
        self.color = ["Black", "White", "Red", "Blue", "Green"]
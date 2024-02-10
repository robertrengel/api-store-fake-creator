from utils.db import db

class ProductModel(db.Model):
    __tablename__ = "product"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.Text)
    image = db.Column(db.String(255))
    images = db.Column(db.ARRAY(db.String(255)))
    price = db.Column(db.Float)
    discount = db.Column(db.Float)
    rating = db.Column(db.Float)
    review = db.Column(db.Integer)
    stock = db.Column(db.Integer)
    sales_count = db.Column(db.Integer)
    create_at = db.Column(db.DateTime)
    
    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'))
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id')) 
    available_sizes_id = db.Column(db.Integer, db.ForeignKey('available_sizes.id'))
    available_color_id = db.Column(db.Integer, db.ForeignKey('available_colors.id'))
    categories_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    seller_id = db.Column(db.Integer, db.ForeignKey('seller.id'))

    available_sizes = db.relationship("SizesModel", back_populates = "products")    
    tag = db.relationship("TagModel", back_populates = "products")
    available_colors = db.relationship('ColorsModel', back_populates = 'products')
    brand = db.relationship('BrandModel', back_populates='products')
    categories = db.relationship('CategoryModel', back_populates='products')
    seller = db.relationship('SellerModel', back_populates='products')
    
    def __init__(self, name, description, image,images, price, discount, rating, review, stock, sales_count, create_at, brand_id, tag_id, available_sizes_id, available_color_id, categories_id, seller_id):
        self.name = name
        self.description = description
        self.image = image
        self.images = images
        self.price = price
        self.discount = discount
        self.rating = rating
        self.review = review
        self.stock = stock
        self.sales_count = sales_count
        self.create_at = create_at
        self.brand_id = brand_id
        self.tag_id = tag_id
        self.available_sizes_id = available_sizes_id
        self.available_color_id = available_color_id
        self.categories_id = categories_id
        self.seller_id = seller_id
        
        

# --> hay que definir los nuevos valores de las rutas
# --> definir valores predeterminados para la base de datos de la tabla color, sizes y tag
# * todas las tabla parecen estar bien creadas
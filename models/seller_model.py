from utils.db import db


class SellerModel(db.Model):
    __tablename__ = "seller"
    
    id = db.Column(db.Integer, primary_key =True)
    name = db.Column(db.String(255))
    store_id = db.Column(db.string(10))
    state = db.Column(db.String(10))
    
    def __init__(self, name, store_id, state):
        self.name = name
        self.store_id = store_id
        self.state = state

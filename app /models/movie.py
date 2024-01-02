from .db import db,environment,SCHEMA,add_prefix_for_prod
from datetime import datetime


class Movies(db.Model):
    __tablename__ = "movies"
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(3000), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    genre = db.Column(db.String(3000), nullable=False)
 
    
    
    # foreign keys 
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False)
    artist_id =db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("artists.id")), nullable=False)
    
    # relationship
    user = db.relationship("User", back_populates="movies")
    artist = db.relationship("Artist", back_populates="movies")
    
    def add_prefix_for_prod(attr):
        if environment == "movies":
            return f"{SCHEMA}.{attr}"
        else:
            return attr

    
    
    
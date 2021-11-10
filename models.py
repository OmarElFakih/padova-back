from flask_sqlalchemy import SQLAlchemy
import json

from sqlalchemy.orm import backref

db = SQLAlchemy()


class House(db.model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    slug = db.Column(db.String(50), unique=True, nullable=False)
    size = db.Column(db.Float, nullable=False)
    featured = db.Column(db.Boolean, nullable=False)
    description = db.Column(db.String(400), nullable=False)
    short_description = db.Column(db.String(200), nullable=False)
    location = db.Column(db.String(100), unique=True, nullable=False)
    minimun_stay = db.Column(db.Integer, nullable=False)
    #facilities
    balcony_terrace = db.Column(db.Boolean, nullable=False)
    garden = db.Column(db.Boolean, nullable=False)
    kitchen = db.Column(db.Boolean, nullable=False)
    pets = db.Column(db.Boolean, nullable=False)
    parking = db.Column(db.Boolean, nullable=False)
    wheelchair = db.Column(db.Boolean, nullable=False)
    basement = db.Column(db.Boolean, nullable=False)
    #amenities
    dishwasher = db.Column(db.Boolean, nullable=False)
    washing_machine = db.Column(db.Boolean, nullable=False)
    dryer = db.Column(db.Boolean, nullable=False)
    ac = db.Column(db.Boolean, nullable=False)
    heating = db.Column(db.Boolean, nullable=False)
    wifi = db.Column(db.Boolean, nullable=False)
    #suitable for 
    students = db.Column(db.Boolean, nullable=False)
    working_proffesionals = db.Column(db.Boolean, nullable=False)
    couples = db.Column(db.Boolean, nullable=False)
    male = db.Column(db.Boolean, nullable=False)
    female = db.Column(db.Boolean, nullable=False)
    #house rules
    smoking = db.Column(db.String(50), unique=True, nullable=False)
    instruments = db.Column(db.String(50), unique=True, nullable=False)
    rooms = db.relationship("Room", backref="House", foreign_keys="Room.house_id")
    images = db.relationship("Picture", backref="House", foreign_keys="Picture.house_id")




class Room(db.model): 
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(50), unique=True, nullable=False)
   slug = db.Column(db.String(50), unique=True, nullable=False)
   image = db.Column(db.String(100), unique=True, nullable=False)
   size = db.Column(db.Float, nullable=False)
   beds = db.Column(db.Integer, nullable=False)
   private_bathroom = db.Column(db.Boolean, nullable=False)
   price = db.Column(db.Float, nullable=False)
   house_id = db.Column(db.Integer, db.ForeignKey("house.id"))





class Picture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(50), unique=True, nullable=False)
    house_id = db.Column(db.Integer, db.ForeignKey("house.id"))

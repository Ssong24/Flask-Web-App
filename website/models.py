from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())  # func gets current date time.
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # ForeignKey: one to many. | sqlalchemy for foreignKey, use small letter even though class name is "User" (with capital letter)



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)  # No same id among users
    email = db.Column(db.String(150), unique=True)  # No user can use same email of other users'
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150)) 
    notes = db.relationship('Note')  # save all different Note in notes.  # When using relationship use class name same (Capital)

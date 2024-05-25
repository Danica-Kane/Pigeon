from.import db
from flask_login import UserMixin
from sqlalchemy.sql import func

from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from wtforms.widgets import TextArea

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    profile_pic = db.Column(db.String(150))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    #user can have many posts
    posts = db.relationship('Posts', backref='poster')

class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(225))
    content = db.Column(db.Text)
    date_posted = db.Column(db.DateTime(timezone=True), default=func.now())
    slug = db.Column(db.String(255))
    #foreign key to link users
    poster_id = db.Column(db.Integer, db.ForeignKey(User.id))
    
class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    content = StringField("Content", validators=[DataRequired()], widget=TextArea())
    slug = StringField("Slug", validators=[DataRequired()])
    submit = SubmitField("Submit")

    
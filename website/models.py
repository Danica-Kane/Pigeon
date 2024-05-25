from.import db
from flask_login import UserMixin
from sqlalchemy.sql import func

from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from wtforms.widgets import TextArea

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
    content = db.Column(db.Text)
    date_posted = db.Column(db.DateTime(timezone=True), default=func.now())
    #foreign key to link users
    poster_id = db.Column(db.Integer, db.ForeignKey(User.id))
    
class PostForm(FlaskForm):
    content = StringField("Content", validators=[DataRequired()], widget=TextArea())
    submit = SubmitField("")

    
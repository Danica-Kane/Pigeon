from flask import Blueprint, flash, render_template, request, session, send_file
from flask_login import login_required, current_user, login_user
from .import db
import os
import uuid
from .models import PostForm, User
from .models import Posts

from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

#csrf = CSRFProtect(views)


views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    
    return render_template("home.html", user=current_user)


@views.route('/instant_msg', methods=['GET', 'POST'])
@login_required
def instant_msg():
    form = PostForm()
    
    if form.validate_on_submit():
        poster = current_user.id
        post = Posts(content=form.content.data, poster_id=poster)
        form.content.data = ""
        
        #add data to database
        db.session.add(post)
        db.session.commit()
    
    # get messages from database
    posts = Posts.query.order_by(Posts.date_posted)
        
    return render_template("instant_msg.html", user=current_user, form=form, posts=posts)

@views.route('/alert_board')
@login_required
def alert_board():
    return render_template("alert_board.html", user=current_user)


@views.route('/event_board')
@login_required
def event_board():
    return render_template("event_board.html", user=current_user)


@views.route('/settings')
@login_required
def settings():
    return render_template("settings.html", user=current_user)

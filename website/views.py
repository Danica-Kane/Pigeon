from flask import Blueprint, flash, render_template, request, session, send_file, redirect, jsonify
from flask_login import login_required, current_user, login_user
from .import db
import os
import uuid
from .models import PostForm, User
from .models import Posts

from .models import PostFormAlert, User
from .models import PostsAlert, User

from .models import PostFormEvent, User
from .models import PostsEvent, User

from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
import time

import pusher

# SET UP PUSHER

pusher_client = pusher.Pusher(
  app_id='1824229',
  key='86898c90b2ecd38da5d5',
  secret='c9341ddc2c68c315b791',
  cluster='us2',
  ssl=True
)

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

@views.route('/message', methods=['POST', 'GET'])
def message():
    
    try : 
        poster = request.form.get('poster')
        content = request.form.get('content')
        date = request.form.get('date')
        
        pusher_client.trigger('chat-channel', 'new-message', {'poster' : poster, 'content': content, 'date' : date})

        
        return jsonify({'result' : 'success'})
    except : 
        return jsonify({'result' : 'failure'})
    

# ALERT BOARD

@views.route('/alert_board', methods=["GET", "POST"])
@login_required
def alert_board():
    
    form = PostFormAlert()
    
    if form.validate_on_submit():
        posteralert = current_user.id
        postalert = PostsAlert(content=form.content.data, title=form.title.data, poster_id=posteralert)
        form.title.data = ""
        form.content.data = ""
        
        #add data to database
        db.session.add(postalert)
        db.session.commit()
    
    # get messages from database
    posts = PostsAlert.query.order_by(PostsAlert.date_posted)
    
    return render_template("alert_board.html", user=current_user,  form=form, posts=posts)

# EVENT BOARD

@views.route('/event_board', methods=["GET", "POST"])
@login_required
def event_board():
    
    form = PostFormEvent()
    
    if form.validate_on_submit():
        posterevent = current_user.id
        postevent = PostsEvent(content=form.content.data, title=form.title.data, entrydate=form.entrydate.data,time=form.time.data, poster_id=posterevent)
        form.title.data = ""
        form.content.data = ""
        form.entrydate.data = ""
        form.time.data = ""   
            
        #add data to database
        db.session.add(postevent)
        db.session.commit()
    
    # get messages from database
    posts = PostsEvent.query.order_by(PostsEvent.date_posted)
    
    return render_template("event_board.html", user=current_user, form=form, posts=posts)

# DELEATE POSTS 

@views.route('delete/<int:id>')
@login_required
def delete(id):
    alert_to_delete = PostsAlert.query.get_or_404(id)
    id = current_user.id

    if id == alert_to_delete.poster_id:
        try:
            db.session.delete(alert_to_delete)
            db.session.commit()
            return redirect('/alert_board')
        except:
            return "there was a problem"
    else:
        flash("you are not authorised to delete this alert. ", category='error')
        return redirect('/alert_board')
    
@views.route('delete_event/<int:id>')
@login_required
def delete_event(id):
    event_to_delete = PostsEvent.query.get_or_404(id)
    id = current_user.id

    if id == event_to_delete.poster_id:
        try:
            db.session.delete(event_to_delete)
            db.session.commit()
            return redirect('/event_board')
        except:
            return "there was a problem"
    else:
        flash("you are not authorised to delete this event. ", category='error')
        return redirect('/event_board')
    
    
@views.route('delete_message/<int:id>')
@login_required
def delete_message(id):
    message_to_delete = Posts.query.get_or_404(id)
    id = current_user.id

    if id == message_to_delete.poster_id:
        try:
            db.session.delete(message_to_delete)
            db.session.commit()
            return redirect('/instant_msg')
        except:
            return "there was a problem"
    else:
        return redirect('/instant_msg')
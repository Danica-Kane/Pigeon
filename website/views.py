from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/instant_msg')
@login_required
def instant_msg():
    return render_template("instant_msg.html", user=current_user)

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


# this is the "web_app/routes/home_route.py" file...

from flask import Blueprint, request, render_template, redirect, flash
from app.rankings import full_rankings


home_route = Blueprint("home_route", __name__)

@home_route.route("/")
@home_route.route("/home")
def index():
    print("HOME...")
    #return "Welcome Home"
    return render_template("bootstrap.html")

@home_route.route("/rankings/dashboard")
def rankings_dashboard():
    rank_list = full_rankings()
    return render_template("rankings_dashboard.html", rank_list=rank_list)


@home_route.route("/player/dashboard")
def player_dashboard():

    return render_template("player_profile_dash.html")


@home_route.route('/handle_data', methods=['POST'])
def handle_data():
    player_name = request.form['playerName']
    print(player_name)
    # Now you can store 'player_name' in a database or pass it to another page or function
    return player_name




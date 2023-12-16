from flask import Blueprint, request, render_template, jsonify
from app.rankings import full_rankings
from app.player_profile import get_player_profile
from app.head_to_head import get_head_to_head 

home_route = Blueprint("home_route", __name__)

# routes that lead to the homepage
@home_route.route("/")
def index():
    return render_template("bootstrap.html")

@home_route.route("/home")
def Home_page():
    return render_template("home.html")

#route that builds the rankings dashboard
@home_route.route("/rankings/dashboard")
def rankings_dashboard():
    try:
        rank_list = full_rankings()
        return render_template("rankings_dashboard.html", rank_list=rank_list)
    except Exception as e:
        # Log the exception and return an error message or redirect
        print(f"Error in rankings_dashboard: {e}")
        return "An error occurred", 500

# route that builds the player profile dashboard
@home_route.route('/player/dashboard')
def player_dashboard():
    return render_template("player_profile_dash.html")

#takes inputs from html and runs player profile script
@home_route.route('/handle_data', methods=['POST'])
def handle_data():
    try:
        player_name = request.form['playerName']
        print(player_name)
        result = get_player_profile(player_name)
        return jsonify({'result': result})
    except Exception as e:
        print(f"Error in handle_data: {e}")
        return jsonify({'error': 'An error occurred'}), 500


# route that builds the head to head dashboard
@home_route.route('/HtoH/dashboard')
def player_head_to_head():
    return render_template("HtoH.html")

#code that recieves the searchbox entries and runs the head to head script
@home_route.route('/submit_data', methods=['POST'])
def submit_data():
    try:
        search1 = request.form.get('search1')
        search2 = request.form.get('search2')
        H2H_result = get_head_to_head(search1, search2)
        return jsonify({'result': H2H_result})
    except Exception as e:
        print(f"Error in submit_data: {e}")
        return jsonify({'error': 'An error occurred'}), 500


# this is the "web_app/routes/rankings_routes.py" file...

from flask import Blueprint, request, render_template, redirect, flash

from app.rankings import get_game_info

rankings_routes = Blueprint("rankings_route", __name__)

@rankings_routes.route("/rankings/dashboard")

def rankings_dashboard():

    try:
        game_info = get_game_info()
        #HERE I NEED TO FIGURE OUT HOW TO GET WHAT I WANT!!!!



        flash("Latest Rankings Data!", "success")
        return render_template("rankings.html", game_info=game_info)
    

    except Exception as err:
        print('OOPS', err)

        flash("Error. Please try again!", "danger")
        return redirect("/")
    

#test
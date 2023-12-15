from flask import Blueprint, request, render_template, redirect, flash

from app.rankings import full_rankings, date, rankings

rankings_routes = Blueprint("rankings_route", __name__)

@rankings_routes.route("/rankings/dashboard", methods=["GET", "POST"])
def rankings_dashboard():
    if request.method == "POST":
        player_name = request.form["player_name"]
        player_id_output = rankings(player_name)
        return render_template("rankings_dashboard.html", player_id=player_id_output)
    else:
        return render_template("rankings_dashboard.html")

if __name__ == "__main__":
    rankings_routes.run(debug=True) 





'''# this is the "web_app/routes/unemployment_routes.py" file...

from flask import Blueprint, request, render_template, redirect, flash

from app.rankings import full_rankings, date

rankings_routes = Blueprint("rankings_route", __name__)



@rankings_routes.route("/rankings/dashboard")
def rankings_dashboard():
    print("RANKINGS DASHBOARD...")

    try:
        data = full_rankings()

        flash("Fetched Latest rankings List!", "success")
        return render_template("rankings_dashboard.html", data=data, date=date)
    
    except Exception as err:
        print('OOPS', err)

        flash("rankings list Error. Please try again!", "danger")
        return redirect("/")

'''

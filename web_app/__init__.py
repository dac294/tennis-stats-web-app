# this is the "web_app/__init__.py" file...

import os

from flask import Flask

from web_app.routes.home_route import home_route
#from web_app.routes.______________ import ____________
#from web_app.______________ import __________
#from web_app.routes.book_routes import book_routes
#from web_app.routes.weather_routes import weather_routes

SECRET_KEY = os.getenv("SECRET_KEY", default="super secret") # set this to something else on production!!!


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = SECRET_KEY

    app.register_blueprint(home_route)
    #app.register_blueprint(unemployment_routes)
    #app.register_blueprint(stocks_routes)
    #app.register_blueprint(book_routes)
    #app.register_blueprint(weather_routes)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)
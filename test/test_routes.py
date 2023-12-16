import pytest
from flask import Flask
from web_app.routes.home_route import home_route

@pytest.fixture
def app():
    app = Flask(__name__, template_folder='web_app/templates')
    app.register_blueprint(home_route)
    app.config.update({
        "TESTING": True,
        # Any other configuration that your blueprint might depend upon
    })
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_index(client):
    response = client.get("/")
    assert response.status_code == 200

def test_rankings_dashboard(client):
    response = client.get("/rankings/dashboard")
    assert response.status_code == 200

# ... similar tests for other routes ...



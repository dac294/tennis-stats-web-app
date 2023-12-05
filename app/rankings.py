from flask import Flask, render_template
import http.client
import json
import datetime as dt
import os 
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

app = Flask(__name__)

def get_game_info(date):
    conn = http.client.HTTPSConnection("api.sportradar.us")
    conn.request("GET", f"https://api.sportradar.com/tennis/trial/v2/en/players/rankings.json?api_key={API_KEY}")

    res = conn.getresponse()
    data = res.read().decode("utf-8")
    json_resp = json.loads(data)
    return json_resp
'''
@app.route('/')
def index():
    date = dt.date.today()
    game_info = get_game_info(date)
    return render_template('index.html', game_info=game_info)

if __name__ == '__main__':
    app.run(debug=True)

'''


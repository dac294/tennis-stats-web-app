import sys
# Append the directory containing 'rankings.py' to sys.path
sys.path.append('/Users/alexcoletti/Documents/GitHub/tennis-stats-web-app/app')
from rankings import rankings
from rankings import get_game_info, rankings 
import datetime as dt
import os
from dotenv import load_dotenv
import pandas as pd
import json

load_dotenv()
API_KEY = os.getenv("API_KEY")
date = dt.date.today()

# need to get player_name from website input!!!!!!!!!!!!!!
def get_player_profile(player_name):

    comp_ID = rankings(player_name)
    print(comp_ID)

    player_link = f"https://api.sportradar.com/tennis/trial/v3/en/competitors/{comp_ID}/profile.json?api_key={API_KEY}"

    player_results = get_game_info(date,player_link)
    print(player_results)
    return(player_results)
    #data = json.dumps(player_results, indent=2)
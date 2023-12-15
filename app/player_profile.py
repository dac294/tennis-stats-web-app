from rankings import rankings
from rankings import get_game_info
import datetime as dt
import os
from dotenv import load_dotenv
import pandas as pd
import json

API_KEY = os.getenv("API_KEY")
date = dt.date.today()

comp_ID = rankings()
print(comp_ID)

player_link = f"https://api.sportradar.com/tennis/trial/v3/en/competitors/{comp_ID}/profile.json?api_key={API_KEY}"

player_results = get_game_info(date,player_link)
print(player_link)
#print(player_results)
data = json.dumps(player_results, indent=2)

print(data)


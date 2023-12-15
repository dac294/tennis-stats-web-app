import http.client
import json
import datetime as dt
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv() #> invoking this function loads contents of the ".env" file into the script's environment...

API_KEY = os.getenv("API_KEY")

date = dt.date.today()

def get_player_id(player_name, dataframe):
    player_row = dataframe[dataframe["player.name"] == player_name]
    if not player_row.empty:
        return player_row.iloc[0]["player.id"]
    else:
        return None

def get_game_info(date, rankings_link):
    conn = http.client.HTTPSConnection("api.sportradar.us")
    conn.request("GET", rankings_link)

    res = conn.getresponse()
    data = res.read().decode("utf-8")
    json_resp = json.loads(data)
    #final_json = json.dumps(json_resp, indent=2)
    return json_resp

def swap_names(player_name):
    # Split the name into first name and last name
    last_name, first_name = player_name.split(", ")
    
    # Format as "firstname lastname"
    return f"{first_name} {last_name}"

def rankings():
    #API_KEY = "3z3vm5s67q4hdabtdmcsxsnd"
    rankings_link = f"https://api.sportradar.com/tennis/trial/v2/en/players/rankings.json?api_key={API_KEY}"

    player_name = input("enter a player: ")

    game_info = get_game_info(date, rankings_link)['rankings']
    #print(json.dumps(game_info, indent=2))  # Print the JSON representation for better readability 

    df = pd.json_normalize(game_info, "player_rankings")

    df["player.name"] = df["player.name"].apply(swap_names)

    player_id_output = get_player_id(player_name, df)

    return player_id_output


if __name__=="__main__":
    rankings_link = f"https://api.sportradar.com/tennis/trial/v2/en/players/rankings.json?api_key={API_KEY}"
    current_rankings = get_game_info(date, rankings_link)
    print(current_rankings)
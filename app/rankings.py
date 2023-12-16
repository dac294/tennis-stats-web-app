import json
import datetime as dt
import pandas as pd
import os
import requests
from dotenv import load_dotenv

load_dotenv() #> invoking this function loads contents of the ".env" file into the script's environment...

API_KEY = os.getenv("API_KEY")

date = dt.date.today()

def get_player_id(player_name, dataframe):
    parts = player_name.split()
    capitalized_parts = [part.capitalize() for part in parts]
    capitalized_full_name = ' '.join(capitalized_parts)
    player_row = dataframe[dataframe["player.name"] == capitalized_full_name]
    if not player_row.empty:
        return player_row.iloc[0]["player.id"]
    else:
        return None

def get_game_info(date, rankings_link):
    try:
        response = requests.get(rankings_link)
        response.raise_for_status()  # This will raise an HTTPError if the HTTP request returned an unsuccessful status code
        data = response.json()  # Directly parse the response to JSON
        return data
    except requests.exceptions.HTTPError as errh:
        print(f"Http Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")
    return None

'''def get_game_info(date, rankings_link):
    conn = http.client.HTTPSConnection("api.sportradar.us")
    conn.request("GET", rankings_link)
    res = conn.getresponse()
    if res.status == 200:
        data = res.read().decode("utf-8")
        return json.loads(data)
    else:
        print(f"API request failed: Status {res.status}")
        return None'''
'''    data = res.read().decode("utf-8")
    json_resp = json.loads(data)
    return json_resp'''

def swap_names(player_name):
    # Split the name into first name and last name
    last_name, first_name = player_name.split(", ")
    
    # Format as "firstname lastname"
    return f"{first_name} {last_name}"

def rankings(player_name):
    #API_KEY = "3z3vm5s67q4hdabtdmcsxsnd"
    rankings_link = f"https://api.sportradar.com/tennis/trial/v2/en/players/rankings.json?api_key={API_KEY}"

    game_info = get_game_info(date, rankings_link)['rankings']
    #print(json.dumps(game_info, indent=2))  # Print the JSON representation for better readability 

    df = pd.json_normalize(game_info, "player_rankings")

    df["player.name"] = df["player.name"].apply(swap_names)

    player_id_output = get_player_id(player_name, df)

    return player_id_output


def full_rankings():
    rankings_link = f"https://api.sportradar.com/tennis/trial/v2/en/players/rankings.json?api_key={API_KEY}"
    current_rankings = get_game_info(date, rankings_link)
    #data = json.dumps(current_rankings, indent=2)
    data = current_rankings
   
    atp_player_info = []
    wta_player_info = []
    for ranking in data["rankings"]:
        for player in ranking["player_rankings"]:
            player_record = {
                "name": player["player"]["name"],
                "rank": player["rank"],
                "ranking_movement": player["ranking_movement"],
                "nationality": player["player"]["nationality"]
            }
            
            if ranking["type"] == "ATP":
                atp_player_info.append(player_record)
            elif ranking["type"] == "WTA":
                wta_player_info.append(player_record)
    print(atp_player_info)
    return atp_player_info

if __name__=="__main__":
    full_rankings()



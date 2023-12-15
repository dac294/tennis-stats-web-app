from rankings import rankings
from rankings import get_game_info
import datetime as dt
import os
import json

from dotenv import load_dotenv

load_dotenv()


API_KEY = os.getenv("API_KEY")
date = dt.date.today()


def get_head_to_head(player1, player2):
    h2h_list2 = [player1, player2]
    h2h_list = []
    for player in h2h_list2:
        comp_ID = rankings(player)
        print(comp_ID)
        h2h_list.append(comp_ID)

    print(h2h_list)

    h2h_link = f"https://api.sportradar.com/tennis/trial/v3/en/competitors/{h2h_list[0]}/versus/{h2h_list[1]}/summaries.json?api_key={API_KEY}"

    h2h_results = get_game_info(date,h2h_link)
    print(h2h_link)
    data = json.dumps(h2h_results, indent=2)
    print(data)
    return h2h_results


if __name__=="__main__":
    get_head_to_head("Novak Djokovic", "Carlos Alcaraz")


from rankings import rankings
from rankings import get_game_info
import datetime as dt
import os
from dotenv import load_dotenv

API_KEY = os.getenv("API_KEY")
date = dt.date.today()



h2h_list = []
for number in range(1,3):
    comp_ID = rankings()
    print(comp_ID)
    h2h_list.append(comp_ID)

print(h2h_list)

h2h_link = f"https://api.sportradar.com/tennis/trial/v3/en/competitors/{h2h_list[0]}/versus/{h2h_list[1]}/summaries.json?api_key={API_KEY}"

h2h_results = get_game_info(date,h2h_link)
print(h2h_link)
print(h2h_results)

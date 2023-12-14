import http.client
import json
import datetime as dt
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()


API_KEY = os.getenv("API_KEY")
date = dt.date.today()


conn = http.client.HTTPSConnection("api.sportradar.com")
live_link = f"https://api.sportradar.com/tennis/trial/v3/en/schedules/live/timelines.json?api_key={API_KEY}"


conn.request("GET", live_link)

res = conn.getresponse()
data = res.read()
json_resp = json.loads(data) 
print(data.decode("utf-8"))













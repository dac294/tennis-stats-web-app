import http.client
from dotenv import load_dotenv

load_dotenv() # go look in the .env file for any env vars

conn = http.client.HTTPSConnection("api.sportradar.com")

conn.request("GET", "/tennis/trial/v3/en/competitions/sr:competition:3101/info.xml?api_key={API_KEY}")

res = conn.getresponse()
data = res.read()

print(data)


if res.status == 200:
    print("Request successful")
else:
    print(f"Request failed with status code: {res.status}")


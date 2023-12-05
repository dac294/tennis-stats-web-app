from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_tennis_stats', methods=['POST'])
def get_tennis_stats():
    player_name = request.form['player_name']

    # Will input the API key in production
    api_key = 'YOUR_API_KEY'
    api_endpoint = 'TENNIS_API_ENDPOINT'

    # Make a request to the Tennis API
    response = requests.get(api_endpoint, params={'player_name': player_name, 'api_key': api_key})

    if response.status_code == 200:
        tennis_stats = response.json()
        return render_template('tennis_stats.html', player_name=player_name, stats=tennis_stats)
    else:
        return render_template('error.html', message=f"Error fetching Tennis stats for {player_name}")

if __name__ == '__main__':
    app.run(debug=True)
'''
    live_matches, upcoming_matches = get_tennis_matches(api_key, api_endpoint)

    if live_matches is not None and upcoming_matches is not None:
        display_matches_summary(live_matches, upcoming_matches)

'''

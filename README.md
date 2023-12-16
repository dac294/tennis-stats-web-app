# tennis-stats-web-app 

This app allows any user to view relevant stats such as the current ATP rankings, individual player information, and head to head data for any two players. 

## Setup: 
### Environment:
You can create and activate a virtual environment by inputting these steps into the command line:
```conda create -n tennis-stats-web-app python=3.10```

```conda activate my-first-env```

Add the relevant packages to the environment:
```pip install -r requirements.txt```

### API:
Obtain an API Key from [SportsRadar](https://developer.sportradar.com/docs/read/tennis/Tennis_v3#tennis-api-overview). By creating an account, you will recieve a temporary API key which you can put in your own ".env" file to properly run the web app.  


## Running the App: 
### Flask:
Create a local server that will run the statistics web app by entering the following info into the command line:
```FLASK_APP=web_app flask run```             

### Python 

Run the Rankings code:
```python app/rankings.py```

Run the Player Profile code:
```python app/player_profile.py```

Run the head to head code: 
```python app/head_to_head.py```


### Pytest:
The code also has a few tests that are used to ensure that the code is working as intended
For example (command line): 
```pytest test/test_routes.py```






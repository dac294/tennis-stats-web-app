
import pandas as pd
from app.rankings import get_player_id, full_rankings

def test_get_player_id():
    sample_data = pd.DataFrame({
        'player.name': ['Roger Federer', 'Rafael Nadal'],
        'player.id': [1, 2]
    })
    player_id = get_player_id('Roger Federer', sample_data)
    assert player_id == 1

    player_id = get_player_id('Unknown Player', sample_data)
    assert player_id is None




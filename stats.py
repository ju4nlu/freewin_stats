import requests

from os import environ

def get_player_details(player_name: str = None) -> dict:
    
    print(f"Getting details of player {player_name}")
    
    if not player_name:
        return {}
    
    player_details_url = 'https://open.faceit.com/data/v4/players'
    
    headers = {
        'accept': 'application/json',
        'Authorization': f'Bearer {environ["FACEIT_DEV_API_KEY"]}',
    }

    params = (
        ('nickname', player_name),
    )

    r = requests.get(player_details_url, 
                    headers=headers, 
                    params=params)
    
    r.raise_for_status()
    
    return r.json()
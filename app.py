from chessdotcom import get_player_game_archives
import requests
import json

def get_all_games_pgn(username):
    data = get_player_game_archives(username).json
    url = data['archives']
    for i in range(len(url)):
        games = requests.get(url[i]).json()
        for j in range(len(games['games'])):
            print(games['games'][j]['pgn'])



get_all_games_pgn('ilvolpe')
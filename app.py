from chessdotcom import get_player_game_archives
import requests
import json

#This function will get all games played by some passed username and write then in a new file, in pgn format (chess notation)
def get_all_games_pgn(username):
    data = get_player_game_archives(username).json
    #This first url give us access to a list, in which every index represents information about games played ina  month
    url = data['archives']
    #The first for loop will itarate over the months, the second over the games in each month
    for i in range(len(url)):
        games = requests.get(url[i]).json()
        for j in range(len(games['games'])):
            with open('games.pgn', 'a') as file:
                file.write(f"{games['games'][j]['pgn']}")


get_all_games_pgn('ilvolpe')
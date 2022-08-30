from chessdotcom import get_player_game_archives
import requests

class Chessdotcom():
    def __init__(self, username):
        self._username = username
    
    def get_achieves(self):
        data = get_player_game_archives(self._username).json
        #This url give us access to a list, in which every index represents information about games played in a certain month, from less to most recent
        url = data['archives']
        return url

    @property
    def get_all_games(self):
        url = self._username.get_achieves()
        #The first for loop will itarate over the months, the second over the games in each month
        for i in range(len(url)):
            games = requests.get(url[i]).json()
            for j in range(len(games['games'])):
                with open('games.pgn', 'a') as file:
                    file.write(f"{games['games'][j]['pgn']}")

ilvolpe = Chessdotcom('ilvolpe')
print(ilvolpe.get_achieves())
from chessdotcom import get_player_game_archives, get_player_stats, get_player_games_by_month_pgn, get_random_daily_puzzle, ChessDotComError
from typing import Optional, Union
import requests

#API Client Module. Chessdotcom class will contain the properties, functions and methods that deal directly with the chessdotcom API 

class Chessdotcom():
    #All validations inside the class will consider ChessDotComError as exception and all API functions return a ChessDotComResponse
    def __init__(self, username):
            self._username = username


    def __str__(self):
        return str(self._username)

    #With this property we'll access all time players archieves, using chessdotcom get_player_game_archives function
    @property
    def archives(self):
        try:
            data = get_player_game_archives(self._username).json
            #This url give us access to a list, in which every index represents information about games played in a certain month, from less to most recent
            if data:
                return data['archives']
            else:
                return "No archeives available"

        except ChessDotComError:
            return "Invalid username"


    @property
    def stats(self):
        try: 
            #Here we use these try and if blocks to ensure that the player exists and has stats available
            if get_player_stats(self._username).json:
                return get_player_stats(self._username).json
            else: 
                return 'No stats found'

        except ChessDotComError:
            return "Invalid username"


    def access_all_games(self):
         try:
            data = get_player_game_archives(self._username).json
            #Here, we access a list of monthly games information
            url = data['archives']
            #The first for loop will itarate over the months and the second over the games in each month
            all_games = ''
            if data:
                for i in range(len(url)):
                    games = requests.get(url[i]).json()
                    for j in range(len(games['games'])):
                        all_games += f"{games['games'][j]['pgn']}"
                return all_games
            else:
                return 'No JSON returned'
         except ChessDotComError:
            return "Invalid input. Check the username."
        

    def games_by_month(self, year: Optional[Union[str, int]], month: Optional[Union[str, int]]):
        try:
            #Access to direct PGN (chess notation) games information 
            data = get_player_games_by_month_pgn(self._username, year, month).json['pgn']['pgn']
            if data:
                return data
            else:
                return 'No JSON returned'
        
        except ChessDotComError:
            return "Invalid input. Check if the username is valid and if the month and year are in the correct format"
    
    #This method return a random daily puzzle from chess.com
    @classmethod
    def random_puzzle(cls):
        return get_random_daily_puzzle()




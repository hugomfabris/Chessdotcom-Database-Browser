from chessdotcom import get_leaderboards, get_player_stats, get_player_game_archives
import requests

def get_most_recent_game(username):
	data = get_player_game_archives(username).json
	url = data['archives'][-1]
	games = requests.get(url).json()
	game = games['games'][-1]
	print(game['pgn'])



get_most_recent_game('ilvolpe')
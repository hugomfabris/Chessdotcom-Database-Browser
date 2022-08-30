
 # ♚ Chess Database Browser ♕

# Description

Chess Database Browser is a python program to import chess games from
chess.com website in PGN format (chess notation, extension for 
softwares like ChessBase), using the chess.com API. With it you can 
download not only a player lifetime database and view any player 
stats. It’s possible to filter the games played in a specific 
month, year, class, and even color. You can also choose a database to
write the links of games played on it and the opening used in 
that game. Moreover, there’s a pretty interesting functionality 
to pick a random chess puzzle and write it on a text file.

# Requirements

### Python 
Version 3.7 or higher

### Libraries/modules

- chessdotcom (pip install chess.com)
- typing (import Optional, Union)
- requests
- datetime (import date, datetime)
- cmd 
- re 

### Chess database software
Some chess software  is needed to visualize the data provided. 
For some resources, such as random puzzle, you can use the internet 
to simulate a chess board.   

## Instalation
1. Clone this repository
2. Install Python 3.7 or higher 
3. Check in the requirements.txt the modules you have and don't have installed       
4. Use pip install on command-line to install the modules you don't 
have yet

## Video Demo:  

<https://youtu.be/iZ2qtcgnuXU>

## Usage/Examples

```cmd
python project.py
Welcome to Chess Database Browser. Type help or ? to list commands.

(Chess) ?

Documented commands (type help <topic>):
========================================
all_games  game_links      games_by_month  opening_links  write_stats
archieves  games_by_class  games_by_year   random_puzzle
close      games_by_color  help            stats        

(Chess) help all_games 
Write in a file standard multi-game format PGN containing all games of a player.
(Chess) stats
Username: MagnusCarlsen
{'stats': {'chess_rapid': {'last': {'rating': 2810, 'date': 1613844867, 'rd': 241}, 'best': {'rating': 2862, 'date': 1418582233, 'game': 'https://www.chess.com/game/live/7498870151'}, 'record': {'win': 5, 'loss': 0, 'draw': 1}}, 'chess_bullet': {'last': {'rating': 3260, 'date': 1607718902, 'rd': 68}, 'best': {'rating': 3350, 'date': 1604349635, 'game': 'https://www.chess.com/game/live/5878212456'}, 'record': {'win': 59, 'loss': 19, 'draw': 11}}, 'chess_blitz': {'last': {'rating': 3189, 'date': 1652202137, 'rd': 102}, 'best': {'rating': 3202, 'date': 1652201571, 'game': 'https://www.chess.com/game/live/5942875338'}, 'record': {'win': 146, 'loss': 32, 'draw': 54}}, 'fide': 2882, 'tactics': {}, 'lessons': {}, 'puzzle_rush': {}}}
(Chess) all_games
Username: MagnusCarlsen
All games by MagnusCarlsen successfully written
(Chess) close
Thank you for using Chess Browser!

```


## Acknowledgements

 - [Documentation](https://chesscom.readthedocs.io/en/latest/)
 - [Publish API details](https://www.chess.com/news/view/published-data-api)
 

import pytest
from functions import write_stats, write_games_by_month, write_all_games, write_games_by_year, write_games_by_class, write_games_by_color
from project import write_game_links, write_opening_links, write_random_puzzle
from datetime import date

def test_write_game_links():
    assert(write_game_links('database-ilvolpe-2021-09.pgn')) == 'database-ilvolpe-2021-09.pgn-links'

def test_write_game_links2():
    assert(write_game_links('non-existing-databse.pgn')) == 'Invalid database'

def test_write_opening_links():
    assert(write_opening_links('database-ilvolpe-2021-09.pgn')) == 'database-ilvolpe-2021-09.pgn-openings'

def test_write_opening_links2():
    assert(write_opening_links('non-existing-databse.pgn')) == 'Invalid database'

def test_write_random_puzzle():
    assert(write_random_puzzle()) == f'random-puzzle-{date.today()}.txt'

def test_write_stats():
    assert(write_stats('ilvolpe')) == f'ilvolpe-stats-{date.today()}.txt'

def test_write_stats2():
    assert(write_stats('invalid-user-to-test')) == 'Invalid username'

def test_write_all_games():
    assert(write_all_games('ilvolpe')) == 'database-ilvolpe.pgn'

def test_write_all_games2():
    assert(write_all_games('invalid-user-to-test')) == 'Invalid input. Check the username.'

def test_write_games_by_month():
    assert(write_games_by_month('ilvolpe', '2016', '04')) == 'No JSON returned'

def test_write_games_by_month2():
    assert(write_games_by_month('ilvolpe', '2047', '04')) == 'Invalid input. Check if the username is valid and if the month and year are in the correct format'

def test_write_games_by_month3():
    assert(write_games_by_month('ilvolpe', '2021', '04')) == 'database-ilvolpe-2021-04.pgn'

def test_write_games_by_month4():
    assert(write_games_by_month('invalid-user-to-test', '2021', '04')) == 'Invalid input. Check if the username is valid and if the month and year are in the correct format'

def test_write_games_by_year():
    assert(write_games_by_year('ilvolpe', '2022')) == 'database-ilvolpe-2022.pgn'

def test_write_games_by_year2():
    assert(write_games_by_year('ilvolpe', '2012')) == 'No games found in 2012'

def test_write_games_by_year3():
    assert(write_games_by_year('ilvolpe', '2099')) == '2099 is a future year'
    
def test_write_games_by_year4():
    assert(write_games_by_year('ilvolpe', '190')) == '190 was before chess.com exists'

def test_write_games_by_year5():
    assert(write_games_by_year('invalid-user-to-test', '2020')) == 'Invalid input. Check if the username is valid and if the month and year are in the correct format'

def test_write_games_by_class():
    assert(write_games_by_class('ilvolpe', 'rapid')) == f'database-ilvolpe-rapid-{date.today()}.pgn'

def test_write_games_by_class2():
    assert(write_games_by_class('ilvolpe', 'invalid-class')) == 'Invalid class'

def test_write_games_by_class3():
    assert(write_games_by_class('invalid-user-to-test', 'bullet')) == 'Invalid username'
    
def test_write_games_by_color():
    assert(write_games_by_color('invalid-user-to-test', 'white')) == 'Invalid username'

def test_write_games_by_color2():
    assert(write_games_by_color('ilvolpe', 'white')) == f'database-ilvolpe-white-games-{date.today()}.pgn'

def test_write_games_by_color3():
    assert(write_games_by_color('ilvolpe', 'blue')) == 'Invalid color'
from apiclient import Chessdotcom
from functions import write_stats, write_games_by_month, write_all_games, write_games_by_year, write_games_by_class, write_games_by_color
import cmd, re
from datetime import date


def main():
    #Execution. Prompts the user using menu module 
    Menu().cmdloop()


#The Menu class organizes the funtionalities of functions.py and apiclient.py modules in order to prompts an user frindly menu on the console 
class Menu(cmd.Cmd):
    intro = 'Welcome to Chess Database Browser. Type help or ? to list commands.\n'
    prompt = '(Chess) '
    
    def do_archieves(self, *args):
        'Prints to the console a list of monthly archives available for a player.'
        input_username = input("Username: ")
        input_username = Chessdotcom(input_username)
        print(input_username.archives)
    
    def do_stats(self, *args):
        "Prints to the console information about the players's ratings, win/loss, and other stats."
        input_username = input("Username: ")
        input_username = Chessdotcom(input_username)
        print(input_username.stats)
    
    def do_write_stats(self, *args):
        "Write in a file information about the players's ratings, win/loss, and other stats."
        input_username = input("Username: ")
        write_stats(input_username)
    
    def do_games_by_month(self, *args):
        'Write in a file standard multi-game format PGN containing all games of a player for a month.'
        input_username = input("Username: ")
        year = input("Year: ")
        month = input("Month: ")
        write_games_by_month(input_username, year, month)
    
    def do_all_games(self, *args):
        'Write in a file standard multi-game format PGN containing all games of a player.'
        input_username = input("Username: ")
        write_all_games(input_username)
    
    def do_games_by_year(self, *args):
        'Write in a file standard multi-game format PGN containing all games of a player for a year.'
        input_username = input("Username: ")
        year = input("Year: ")
        write_games_by_year(input_username, year)
    
    def do_games_by_class(self, *args):
        'Write in a file standard multi-game format PGN containing all games of a player for a class.'
        input_username = input("Username: ")
        time_class = input("Time class: ")
        write_games_by_class(input_username, time_class) 
    
    def do_games_by_color(self, *args):
        'Write in a file standard multi-game format PGN containing all games of a player for a given color.'
        input_username = input("Username: ")
        color = input("Color: ")
        write_games_by_color(input_username, color)
    
    def do_game_links(self, *args):
        'Write a file containing all game links of a given PGN database.'
        database = input('Choose an existing database: ')
        write_game_links(database)
    
    def do_opening_links(self, *args):
        'Write a file containing all openings played in a given PGN database.'
        database = input('Choose an existing database: ')
        write_opening_links(database)
    
    def do_random_puzzle(self, *args):
        'Write a file, in FEN notation, a random chess puzzle. If used more than once in a day, appends a new puzzle to the existing file'
        write_random_puzzle()
        
    def do_close(self, *args):
        'Exit the programm'
        print('Thank you for using Chess Browser!')
        return True

    
    
def write_game_links(database):
    try:    
        with open(database, 'r') as file:
            lines = file.readlines()
            for line in lines:
                date = re.match(r'\[Date \"\d\d\d\d\.\d\d\.\d\d\"\]', line)
                link = re.match(r'\[Link \"https\:\/\/www\.chess\.com\/game\/live\/[\d]+\"\]', line)
                with open(f'{database}-links', 'a') as output:
                    if date:
                        output.write(f'{date.group()}\n')
                    elif link:
                        output.write(f'{link.group()}\n')
            print(f'Links successfully written written')
            return f'{database}-links'
    except FileNotFoundError:
        print("Invalid database")
        return 'Invalid database'


def write_opening_links(database):
    try:
        with open(database, 'r') as file:
            lines = file.readlines()
            for line in lines:
                date = re.match(r'\[Date\s\"\d\d\d\d\.\d\d\.\d\d\"\]', line)
                opening = re.match(r'\[ECOUrl \"https\:\/\/www\.chess\.com\/openings\/.+"\]', line)
                with open(f'{database}-openings', 'a') as output:
                    if date:
                        output.write(f'{date.group()}\n')
                    elif opening:
                        output.write(f'{opening.group()}\n')
            print(f'Opening links successfully written')
            return f'{database}-openings'
    except FileNotFoundError:
        print("Invalid database")
        return 'Invalid database'


def write_random_puzzle():
    with open(f'random-puzzle-{date.today()}.txt', 'a') as file:
        random_puzzle = str(Chessdotcom.random_puzzle())
        title = re.search(r"title=[\'\"](.+?)[\'\"]", random_puzzle)
        fen = re.search(r"\[FEN \"(.+?)\'", random_puzzle)
        file.write(f'{title.group()}\n')
        file.write(f'{fen.group()}\n')
    print('Puzzle successfully generated')
    return f'random-puzzle-{date.today()}.txt'

if __name__ == "__main__":
    main()
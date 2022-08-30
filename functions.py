from apiclient import Chessdotcom
from datetime import date, datetime
import requests

# Wrapper module. Used for handling, analyzing and quering data obtained from the chess.com through the API Client Module apiclient.py


def write_stats(username):
    username = Chessdotcom(username)
    #Here we call the stats method right after creating the file to use the method's validation. This pattern will be used on the other funtions
    username.stats
    if username.stats != 'Invalid username':
        with open(f'{username}-stats-{date.today()}.txt', 'w') as file:
            file.write(str(username.stats))
        print(f'Stats by {username} successfully written')
        return f'{username}-stats-{date.today()}.txt'
    else:
        print('Invalid username')
        return "Invalid username"

def write_all_games(username):
    username = Chessdotcom(username)
    if username.access_all_games() != 'No JSON returned' and username.access_all_games() != "Invalid input. Check the username.":
        with open(f'database-{username}.pgn', 'a') as file:
            file.write(username.access_all_games())
        print(f'All games by {username} successfully written')
        return f'database-{username}.pgn'
    else:
        return username.access_all_games()


def write_games_by_month(username, year, month):
    month = int(month)
    username = Chessdotcom(username)
    data = username.games_by_month(year, month)
    if data == 'No JSON returned' or data == "Invalid input. Check if the username is valid and if the month and year are in the correct format":
        print(data)
        return data
    else:
        with open(f'database-{username}-{year}-{month:02d}.pgn', 'a') as file:
            file.write(data)
        print(f'Games by {username} successfully written')
        return f'database-{username}-{year}-{month:02d}.pgn'


def write_games_by_year(username, year):
    username = Chessdotcom(username)
    count = 0
    #To avoid error due to upcoming months in a year, we use this if block
    if year == str(datetime.now().year):
        #This count variable will help to log on  the console that no games was found in this year whan it's the case
        for _ in range(1, (datetime.now().month)):
            tempdata = username.games_by_month(year, _)
            if tempdata == 'No JSON returned':
                count += 1
                pass
            else: 
                with open(f'database-{username}-{year}.pgn', 'a') as file:
                    file.write(tempdata)
                return f'database-{username}-{year}.pgn'
        if count == datetime.now().month:
                return f"No games found in {year}"
    elif int(year) > int(datetime.now().year):
        print(f'{year} is a future year')
        return f'{year} is a future year'
    elif int(year) < 2000:
        print(f'{year} was before chess.com exists')
        return f'{year} was before chess.com exists'
    elif username.games_by_month(year, 1) == "Invalid input. Check if the username is valid and if the month and year are in the correct format":
        return "Invalid input. Check if the username is valid and if the month and year are in the correct format"
    else:

        for _ in range(1, 13):
            tempdata = username.games_by_month(year, _)
            if tempdata == 'No JSON returned':
                count += 1
                pass
            else: 
                with open(f'database-{username}-{year}.pgn', 'a') as file:
                    file.write(tempdata)
                print(f'Games by {username} successfully written')
                return f'database-{username}-{year}.pgn'
        if count == 12:
            print(f"No games found in {year}")
            return f"No games found in {year}"
            

def write_games_by_class(username, time_class):
    username = Chessdotcom(username)
    url = username.archives
    if time_class in ['rapid', 'bullet', 'blitz']:
        if url != 'No archeives available' and url != 'Invalid username':
            #The first for loop will itarate over the months, the second over the games in each month
            for i in range(len(url)):
                games = requests.get(url[i]).json()
                for j in range(len(games['games'])):
                    with open(f'database-{username}-{time_class}-{date.today()}.pgn', 'a') as file:
                        if f"{games['games'][j]['time_class']}" == time_class:
                            file.write(f"{games['games'][j]['pgn']}")
                    print(f'Games by {username} successfully written')
                    return f'database-{username}-{time_class}-{date.today()}.pgn'
        else:
            return url
    else:
        return 'Invalid class'


def write_games_by_color(username, color):
    username = Chessdotcom(username)
    url = username.archives
    if username.archives == "Invalid username":
        print('Invalid username')
        return 'Invalid username'
    else:    
        for i in range(len(url)):
            games = requests.get(url[i]).json()
            for j in range(len(games['games'])):
                if color in ['white', 'black']:
                    with open(f'database-{username}-{color}-games-{date.today()}.pgn', 'a') as file: 
                        if color == 'white':
                            if f"{games['games'][j]['white']['username']}" == str(username):
                                file.write(f"{games['games'][j]['pgn']}")
                        else:
                            if f"{games['games'][j]['black']['username']}" == str(username):
                                file.write(f"{games['games'][j]['pgn']}")
                else:
                    print('Invalid color')
                    return 'Invalid color'
        print(f'Games by {username} successfully written')
        return f'database-{username}-{color}-games-{date.today()}.pgn'
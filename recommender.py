#!/usr/bin/python

import pandas as pd
from IPython.display import display

vg_data = pd.read_csv("games-data.csv")
#formats data to only lowercase
vg_data['name'] = vg_data['name'].str.lower()
vg_data['platform'] = vg_data['platform'].str.lower()

def find_game(game_name):
    
    while not game_name in vg_data['name'].unique():
        game_name = input('Could not find game. Try entering again:\n').lower()

    #turns that data into a game entry
    game = vg_data.loc[vg_data['name'] == game_name]

    if game.shape[0] > 1:
        #we only want one game, so we find which game the user meant
        platform = input('Found duplicates of game specified. What platform was your game released on?\n').lower()
        #make sure user inputed a valid platform name
        while not platform in vg_data['platform'].unique():
            platform = input('Could not find platform. Try entering again:\n').lower()

        game = game.loc[game['platform'] == platform]
    
    return game


#finds the user's favorite game
game1 = find_game(input('What is your favorite video game released on or before November 2020?\n').lower())

#does the same for the second favorite game and the third
game2 = find_game(input('What is your second favorite video game released on or before November 2020?\n').lower())
game3 = find_game(input('What is your third favorite video game released on or before November 2020?\n').lower())

user_games = [game1, game2, game3]

#dictionaries counting the frequency of genres and publishers from user data
genre_frequency = {}
publisher_frequency = {}

for game in user_games:
    # [0,6] is the location of the genre of the game
    all_genres = game.iloc[0,6]
    #list of every single genre
    genres = all_genres.split(',')

    for genre in genres:
        if genre in genre_frequency:
            genre_frequency[genre] += 1
        else:
            genre_frequency[genre] = 1
print(genre_frequency)

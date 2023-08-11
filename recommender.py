import pandas as pd

vg_data = pd.read_csv("games-data.csv")
#formats data to only lowercase
vg_data['name'] = vg_data['name'].str.lower()

game_1 = input('What is your favorite video game released on or before November 2020?\n').lower()
while not game_1 in vg_data['name'].unique():
    game_1 = input('Could not find game. Try entering again:\n').lower()

game_2 = input('What is your second favorite video game released on or before November 2020?\n').lower()
while not game_2 in vg_data['name'].unique():
    game_2 = input('Could not find game. Try entering again:\n').lower()

game_3 = input('What is your third favorite video game released on or before November 2020?\n').lower()
while not game_3 in vg_data['name'].unique():
    game_3 = input('Could not find game. Try entering again:\n').lower()

#user_games = [vg_data[game_1], game_], game_3]
    
#dictionaries counting the frequency of genres and publishers from user data
genre_frequency = {}
publisher_frequency = {}

#print(vg_data.loc[vg_data['name'] == game_1])


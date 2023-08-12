import pandas as pd
from IPython.display import display

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

user_games = [game_1, game_2, game_3]

#dictionaries counting the frequency of genres and publishers from user data
genre_frequency = {}
publisher_frequency = {}

all_genres = vg_data.loc[vg_data['name'] == game_1]
display(all_genres)
#print(vg_data.loc[vg_data['name'] == game_1])
#for game in user_games:
    #creates string containing all the genres of the game
 #   all_genres = vg_data.loc[vg_data['name'] == game]['genre']
  #  genres = all_genres.split(',')

   # for genre in genres:
    #    if genre in genre_frequency:
     #       genre_frequency[genre] += 1
      #  else:
       #     genre_frequency[genre] = 0

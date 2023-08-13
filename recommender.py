import pandas as pd
import numpy as np

from IPython.display import display

vg_data = pd.read_csv("games-data.csv")
# formats data to only lowercase
vg_data['name'] = vg_data['name'].str.lower()
vg_data['platform'] = vg_data['platform'].str.lower()

def find_game(game_name):
    
    while not game_name in vg_data['name'].unique():
        game_name = input('Could not find game. Try entering again:\n').lower()

    # turns that data into a game entry
    game = vg_data.loc[vg_data['name'] == game_name]

    if game.shape[0] > 1:
        # we only want one game, so we find which game the user meant
        platform = input('Found duplicates of game specified. What platform was your game released on?\n').lower()
        # make sure user inputed a valid platform name
        while not platform in vg_data['platform'].unique():
            platform = input('Could not find platform. Try entering again:\n').lower()

        game = game.loc[game['platform'] == platform]
    
    return game.squeeze()

# function that checks whether a series is in a container of series
def series_is_in(series, container):
    for x in container:
        if series.equals(x):
            return True
    return False

# finds the user's favorite game
game1 = find_game(input('What is your favorite video game released on or before November 2020?\n').lower())
# does the same for the second favorite game and the third
game2 = find_game(input('What is your second favorite video game released on or before November 2020?\n').lower())
game3 = find_game(input('What is your third favorite video game released on or before November 2020?\n').lower())

user_games = [game1, game2, game3]

# dictionaries counting the frequency of genres and developers from user data
genre_frequency = {}
developer_frequency = {}

for game in user_games:
    # genres is a list of all the genres this game has
    genres = game['genre'].split(',')
    for genre in genres:
        if genre in genre_frequency:
            genre_frequency[genre] += 1
        else:
            genre_frequency[genre] = 1
    
    # now counts developer
    dev = game['developer']
    if dev in developer_frequency:
        developer_frequency[dev] += 1
    else:
        developer_frequency[dev] = 1

# new column for the data to see how well they rank with the user's preferences
score = np.zeros(vg_data.shape[0])

print('...')
for index, row in vg_data.iterrows():
    # Don't want to suggest games the user inputted
    if series_is_in(row, user_games):
        score[index] = float('-inf')
    else:
        score[index] = 0
        # list of the current genres
        genres = row['genre'].split(',')
        for genre in genres:
            if genre in genre_frequency:
                # 0.5 is an arbitrary value chosen as the weight of each genre
                score[index] += genre_frequency[genre] * 0.5
        
        dev = row['developer']
        # checks developer
        if dev in developer_frequency:
            # 0.33 is an arbitrary value chosen as the weight of each developer
            score[index] += developer_frequency[dev] * 0.33

# adds score as a column to video game data
vg_data['generated_score'] = score

# sorts the suggestions based on the scores and its user rating
vg_data = vg_data.sort_values(by=['generated_score', 'user score'], ascending=False)

# gets number of suggestions from user
print('Calculations complete')
num_suggestion = int(input('How many suggestions would you like?\n'))
while num_suggestion > vg_data.shape[0] and num_suggestion <= 0:
    num_suggestion = input('Input too high or too low. Please try again\n')
    
vg_data = vg_data.drop(['developer', 'players', 'critics', 'users', 'r-date', 'platform', 'genre', 'score'], axis=1)
display(vg_data[:num_suggestion])
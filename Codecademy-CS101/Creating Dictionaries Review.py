songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

# Combine our two lists together using zip
zip_songs_playcounts = zip(songs, playcounts)

# List comprehension to join our two lists into a key, value pair
plays = {key:value for key, value in zip(songs, playcounts)}
print(plays, '\n')

# Adds 'Purple Haze' with key '1' to plays and 'Respect' with '94'
plays['Purple Haze'] = 1
plays['Respect'] = 94

empty_dictionary = {}

# Library dictionary with our plays dictioanry as a value pair, as-well as 'Sunday Feelings' with an empty dictioanry which can be ammended later
library = {'The Best Songs': plays, 'Sunday Feelings': empty_dictionary}
print(library)

from math import ceil
# Report functions


# Import all games in a double list
def import_games(file_name):
    game_list = []
    with open(file_name, 'r') as the_file:
        for line in the_file:
            game_list.append(line.strip().split('\t'))
    return game_list


# Get most played game in the file
def get_most_played(file_name):
    SOLD_COPIES = 1
    TITLE = 0
    game_list = import_games(file_name)
    sold_copies_list = [float(game[SOLD_COPIES]) for game in game_list]
    most_sold = max(sold_copies_list)
    most_played_game = [game[TITLE] for game in game_list if most_sold == float(game[SOLD_COPIES])]
    return most_played_game[TITLE]


# Returns how many copies has been sold
def sum_sold(file_name):
    SOLD_COPIES = 1
    total_copies_sold = 0
    game_list = import_games(file_name)
    sold_copies_list = [float(game[SOLD_COPIES]) for game in game_list]
    for copies in sold_copies_list:
        total_copies_sold += copies
    return total_copies_sold


# Average sold copies
def get_selling_avg(file_name):
    number_of_games = 0
    game_list = import_games(file_name)
    total_sold_copies = sum_sold(file_name)
    for each_game in game_list:
        number_of_games += 1
    return total_sold_copies / number_of_games


# Counting the longest title
def count_longest_title(file_name):
    TITLE = 0
    game_title_list = []
    count_char_title = 0
    longest_title = ''
    game_list = import_games(file_name)
    game_title_list = [game[TITLE] for game in game_list]
    longest_title = max(game_title_list, key=len)
    for char in longest_title:
        count_char_title += 1
    return count_char_title


# Average of the release dates
def get_date_avg(file_name):
    RELEASE_YEAR = 2
    game_list = import_games(file_name)
    release_date_list = [int(game[RELEASE_YEAR]) for game in game_list]
    return ceil(sum(release_date_list) / len(release_date_list))


# Get game properties by title
def get_game(file_name, title):
    TITLE = 0
    GET_LIST_PROPERTIES = 0
    all_properties_from_title = []
    game_list = import_games(file_name)
    game_properties = [game for game in game_list if str(title) == game[TITLE]]
    for properties in game_properties[GET_LIST_PROPERTIES]:
        if properties.isdigit():
            all_properties_from_title.append(int(properties))
        elif properties.replace('.', '').isdigit():
            all_properties_from_title.append(float(properties))
        else:
            all_properties_from_title.append(properties)
    return all_properties_from_title


# Dictionary of numbers of genres found in file
def count_grouped_by_genre(file_name):
    GENRE = 3
    count_genre = 0
    genre_dictionary = {}
    game_list = import_games(file_name)
    games_genre = [game[GENRE] for game in game_list]
    unique_genre = list(set(games_genre))
    for genre in unique_genre:
        count_genre = 0
        for game in game_list:
            if genre == game[GENRE]:
                count_genre += 1
        genre_dictionary[genre] = count_genre
    return genre_dictionary


# 
def get_date_ordered(file_name):
    RELEASE_YEAR = 2
    TITLE = 0
    game_list = import_games(file_name)
    sorted_game_titles = []

    game_list.sort(key = lambda x: x[2])
    for game in game_list:
        if 
        sorted_game_titles.append(game[TITLE]) 
    return sorted_game_titles[::-1]
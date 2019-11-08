# Report functions
# Import file lines in a double list
def import_game_stats(file_name):
    game_list = []
    with open(file_name, 'r') as file:
        for line in file:
            game_list.append(line.strip().split("\t"))
        return game_list


# Count how many games are in the list
def count_games(file_name):
    COUNT_HOW_MANY_GAMES = 0
    with open(file_name, 'r') as the_file:
        for line in the_file:
            COUNT_HOW_MANY_GAMES += 1
    return COUNT_HOW_MANY_GAMES


# Checks if there is a game of given year
def decide(file_name, year):
    GAME_YEAR = 2
    game_list = import_game_stats(file_name)
    for each_game in game_list:
        if str(year) == each_game[GAME_YEAR]:
            return True
    return False


# Returns the latest game by year
def get_latest(file_name):
    TITLE = 0
    YEAR = 2
    game_list = import_game_stats(file_name)
    year_list = []
    latest_game = 0
    for game in game_list:
        year_list.append(game[YEAR])
    latest_game = max(year_list)
    for game in game_list:
        if str(latest_game) == game[YEAR]:
            return game[TITLE]


# Show how many games are by genre
def count_by_genre(file_name, genre):
    count_genre = 0
    GENRE = 3
    game_list = import_game_stats(file_name)
    for game in game_list:
        if str(genre) in game[GENRE]:
            count_genre += 1
    return count_genre


# Return line number from given title
def get_line_number_by_title(file_name, title):
    TITLE = 0
    count_line = 0
    game_list = import_game_stats(file_name)
    for game in game_list:
        count_line += 1
        if str(title) in game[TITLE]:
            return count_line
    raise ValueError


#
def sort_abc(file_name):
    game_title_list = []
    TITLE = 0
    game_list = import_game_stats(file_name)
    for game in game_list:
        game_title_list.append(game[TITLE])
    return sorted(game_title_list)

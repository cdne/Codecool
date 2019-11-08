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
    RELEASE_YEAR = 2
    game_list = import_game_stats(file_name)
    for each_game in game_list:
        if str(year) == each_game[RELEASE_YEAR]:
            return True
    return False


# Returns the latest game by year
def get_latest(file_name):
    TITLE = 0
    RELEASE_YEAR = 2
    game_list = import_game_stats(file_name)
    year_list = []
    latest_game = 0
    for game in game_list:
        year_list.append(game[RELEASE_YEAR])
    latest_game = max(year_list)
    for game in game_list:
        if str(latest_game) == game[RELEASE_YEAR]:
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


def sort_abc(file_name):
    game_title_list = []
    TITLE = 0
    game_list = import_game_stats(file_name)
    for game in game_list:
        game_title_list.append(game[TITLE])

    for first in range(len(game_title_list)):
        for second in range(0, len(game_title_list) - first - 1):
            if game_title_list[second] > game_title_list[second + 1]:
                game_title_list[second], game_title_list[second + 1] = game_title_list[second + 1], game_title_list[second]

    return game_title_list
    # return sorted(game_title_list)


# Get all genres
def get_genres(file_name):
    genre_list = []
    GENRE = 3
    game_list = import_game_stats(file_name)
    for game in game_list:
        genre_list.append(game[GENRE])
    return bubble_sort(list(set(genre_list)))


# Get release date for top sold fps game
def when_was_top_sold_fps(file_name):
    COPIES_SOLD = 1
    RELEASE_YEAR = 2
    GENRE = 3
    top_copies_sold = 0
    copies_sold = []
    fps_games = []
    game_list = import_game_stats(file_name)
    try:
        fps_games = [game for game in game_list if 'First-person shooter' == game[GENRE]]
        copies_sold = [float(game[COPIES_SOLD]) for game in fps_games]
        top_copies_sold = max(copies_sold)
        for game in game_list:
            if str(top_copies_sold) == game[COPIES_SOLD]:
                return int(game[RELEASE_YEAR])
    except ValueError:
        raise ValueError

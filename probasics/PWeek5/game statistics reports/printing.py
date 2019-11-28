from reports import *
from export import *
import os

# Printing functions

while True:
    os.system('clear')
    print("\n\n1. How many games are in the file?")
    print("2. Is there a game from a given year?")
    print("3. Which was the latest game?")
    print("4. How many games do we have by genre?")
    option = int(input("Enter your option: "))
    if option == 1:
        print(count_games('game_stat.txt'))
        answer = input("Do you want to export it to the file ? (yes)")
        if answer == 'yes':
            export_data(count_games('game_stat.txt'))
            print("Data was exported to exported_data.txt")
        else:
            print("You didn't enter as instructed")
        input('Press enter to continue ...')
    elif option == 2:
        year = input("Enter the year so we can show if is found in the file: ")
        print(decide('game_stat.txt', year))  
        answer = input("Do you want to export it to the file ? (yes/no): ")
        if answer == 'yes':
            export_data(decide('game_stat.txt', year))
            print("Data was exported to exported_data.txt")
        else:
            print("You didn't enter as instructed")
        input('Press enter to continue ...')
    elif option == 3:
        print(get_latest('game_stat.txt'))  
        answer = input("Do you want to export it to the file ? (yes/no): ")
        if answer == 'yes':
            export_data(get_latest('game_stat.txt'))
            print("Data was exported to exported_data.txt")
        else:
            print("You didn't enter as instructed")
        input('Press enter to continue ...')
    elif option == 4:
        genre = input('Enter desired genre: ')
        print(count_by_genre('game_stat.txt', genre)) 
        answer = input("Do you want to export it to the file ? (yes/no): ")
        if answer == 'yes':
            export_data(count_by_genre('game_stat.txt', genre))
            print("Data was exported to exported_data.txt")
        else:
            print("You didn't enter as instructed")
        input('Press enter to continue ...')
# export_data(count_games('game_stat.txt'))
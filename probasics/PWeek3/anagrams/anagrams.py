import csv
import sys

INDEX_0 = 0
GET_FIRST_COMMAND_LINE_ARGUMENT = 1


# importing each line from csv in a list
def import_lines(filename):
    try:
        word_list = []
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            word_list = list(reader)
        return word_list
    except IOError:
        print("File does not exist")
        exit()


# printing anagrams of specific word
def show_anagrams(imported_list):
    for word in imported_list:
        for word2 in imported_list:
            if sorted(word[INDEX_0]) == sorted(word2[INDEX_0]):
                print(f'{word2[INDEX_0]} is an anagram of {word[INDEX_0]}')


# running script
try:
    show_anagrams(import_lines(sys.argv[GET_FIRST_COMMAND_LINE_ARGUMENT]))
except IndexError:
    print('Error - you didn\'t choose a file to import')

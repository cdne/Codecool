import sys

FIRST_ARGUMENT = 1
SECOND_ARGUMENT = 2
FILE = 'ideas.txt'

def get_input():
    idea = input('What is your new idea: ')
    return idea

def read_ideas(file_name):
    with open(file_name, 'r') as the_file:
        all_ideas = the_file.readlines()
        clean_ideas = [idea.replace('\n', '') for idea in all_ideas]
        return clean_ideas


def add_ideas(file_name):
    with open(file_name, 'a+') as the_file:
        new_idea = get_input()
        the_file.writelines(new_idea + '\n')


def write_ideas(file_name, new_ideas):
    with open(file_name, 'w+') as the_file:
        for idea in new_ideas:
            the_file.writelines(idea + '\n')


def get_remove_input():
    try:
        if sys.argv[SECOND_ARGUMENT].isdigit():
            return int(sys.argv[SECOND_ARGUMENT])
    except IndexError:
        return None


def remove_ideas(idea_to_remove):
    my_ideas = read_ideas(FILE)
    for index in range(len(my_ideas)):
        if index + 1 == idea_to_remove:
            my_ideas.pop(index)
    return my_ideas


def print_ideas(ideas):
    print('Your ideabank:')
    for index in range(len(ideas)):
        print(f'{index+1}.{ideas[index]}')


def ideabank():
    try:
        if sys.argv[FIRST_ARGUMENT] == '--list':
            print_ideas(read_ideas(FILE))
        elif sys.argv[FIRST_ARGUMENT] == '--delete':
            idea_to_remove = get_remove_input()
            new_ideas_list = remove_ideas(idea_to_remove)
            write_ideas(FILE, new_ideas_list)
    except IndexError:
        add_ideas(FILE)
        print_ideas(read_ideas(FILE))


ideabank()
import sys

ARGUMENT = 1

def hello_world():
    if len(sys.argv) > 1:
        print_funct(sys.argv[ARGUMENT])
    else:
        print_funct('World')

def print_funct(name):
    print(f'Hello {name}!')

hello_world()
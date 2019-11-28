def fibonacci_sequence(number_of_times):
    number1, number2 = 0, 1
    for count in range(number_of_times):
        print_sequence(count, number1)
        result = number1 + number2
        number1 = number2
        number2 = result


def print_sequence(count, number):
    print(f'{count+1:>2}:{number:>10}')


def get_input():
    while True:
        try:
            number_of_times = int(input(
                'How many numbers you want to print?: '
            ))
        except ValueError:
            print_error()
            continue
        else:
            return number_of_times
            break


def print_error():
    print('You didn\'t enter a number')


def main():
    if __name__ == '__main__':
        amount = get_input()
        fibonacci_sequence(amount)


main()
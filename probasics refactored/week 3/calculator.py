def calaculator():
    start_calculator = True
    while start_calculator:
        number_one = number_input('first')
        operator = operator_input()
        number_two = number_input('second')
        result = calculate(number_one, operator, number_two)
        print_result(result)
        start_calculator = try_again()


def number_input(text):
    while True:
        try:
            number = int(input(f'Enter {text} number: '))
        except ValueError:
            print_error()
            continue
        else:
            return number
            break


def operator_input():
    operators = ['-', '+', '*', '/']
    while True:
        operator = input('Enter one of this operators(- + * /): ')
        if operator in operators:
            return operator
            break
        else:
            print_error()
            continue


def calculate(number_one, operator, number_two):
    try:
        if operator == '-':
            return number_one - number_two
        elif operator == '+':
            return number_one + number_two
        elif operator == '*':
            return number_one * number_two
        elif operator == '/':
            return number_one / number_two
    except TypeError:
        print_error()


def try_again():
    option = input('Do you want to try again ? (y/n): ')
    if 'y' == option.strip():
        return True
    else:
        return False


def print_error():
    print('You didn\'t enter as instructed.')


def print_result(result):
    print(f'Result is {result}')


def main():
    if __name__ == '__main__':
        calaculator()

main()

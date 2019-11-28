def calaculator():
    start_calculator = True
    while start_calculator:
        number_one = valid_number()
        operator = valid_operator()
        number_two = valid_number()
        result = calculate(number_one, operator, number_two)
        print_result(result)
        start_calculator = try_again()


def number_input():
    number = int(input(f'Enter number: '))
    return number


def valid_number():
    while True:
        try:
            number = number_input()
        except ValueError:
            print_error()
            continue
        else:
            return number
            break


def operator_input():
    operator = input('Enter one of this operators(- + * /): ')
    return operator


def valid_operator():
    operators = ['-', '+', '*', '/']
    while True:
        operator = operator_input()
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

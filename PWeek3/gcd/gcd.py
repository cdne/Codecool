number_one = int(input("Enter first number: "))
number_two = int(input("Enter second number: "))
listOfNumbers = []
number_oneDiv = []
number_twoDiv = []


# generates a list of numbers
for i in range(1, 30000):
    listOfNumbers.append(i)


z = 1
while z < len(listOfNumbers):
    if number_one % z == 0:
        number_oneDiv.append(z)
    if number_two % z == 0:
        number_twoDiv.append(z)
    z += 1

print("Common divisior is/are: ", list(set(number_oneDiv).intersection(set(number_twoDiv))))
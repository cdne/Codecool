
# declaring variables
numberList = []
counter = 1
z = 0


# geenerate 201 numbers in list
for i in range(0, 201):
    numberList.append(i)
while z < len(numberList):
    if numberList[z] % 7 == 0 or numberList[z] % 9 == 0:
        result = numberList[z]
        counter += 1
        if(counter <= 26):
            print(f'{counter-1}. {result}')
    z += 1

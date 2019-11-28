import random

diceOne = random.randrange(1,6)
diceTwo = random.randrange(1,6)
diceThree = random.randrange(1,6)
diceFour = random.randrange(1,6)
diceFive = random.randrange(1,6)

# # basic roll
# print('Attacker: {0}-{1}-{2}'.format(diceOne,diceTwo,diceThree))
# print('Defender: {0}-{1}'.format(diceFour,diceFive))


# variations 1
# print("Dice:")
# print('      Attacker: {0}-{1}-{2}'.format(diceOne,diceTwo,diceThree))
# print('      Defender: {0}-{1}\n'.format(diceFour,diceFive))

# print("Outcome:")
# if diceOne > diceFour and diceTwo > diceFive:
#     print('      Attacker: Lost 0 points')
# elif diceOne < diceFour and diceTwo > diceFive or diceOne > diceFour and diceTwo < diceFive:
#     print('      Attacker: Lost 1 point')
# elif diceOne == diceFour and diceTwo > diceFive:
#     print('      Attacker: Lost 1 point')
# elif diceOne == diceFour and diceTwo == diceFive:
#     print('      Attacker: Lost 2 point')
# elif diceOne == diceFour and diceTwo < diceFive: 
#     print('      Attacker: Lost 2 point')
# elif diceOne > diceFour and diceTwo == diceFive: 
#     print('      Attacker: Lost 1 point')
# else:
#     print('      Attacker: Lost 2 point')

# if diceFour >= diceOne and diceFive >= diceTwo:
#     print('      Defender: Lost 0 point')
# elif diceFour >= diceOne and diceFive < diceTwo or diceFour < diceOne and diceFive > diceTwo:
#     print('      Defender: Lost 1 point')
# else:
#     print('      Attacker: Lost 2 point') 

# variations 2

firstQuestion = int(input("How many units attack: "))
secondQuestion = int(input("How many units defend: "))

if firstQuestion == 3 and secondQuestion == 2 or firstQuestion == 2 and secondQuestion == 3:
    print("Dice:")
    if firstQuestion == 3 and secondQuestion == 2:
        print('      Attacker: {0}-{1}-{2}'.format(diceOne,diceTwo,diceThree))
        print('      Defender: {0}-{1}\n'.format(diceFour,diceFive))
    elif firstQuestion == 2 and secondQuestion == 3:
        print('      Attacker: {0}-{1}'.format(diceOne,diceTwo,diceThree))
        print('      Defender: {0}-{1}\n'.format(diceFour,diceFive))
                   

    print("Outcome:")
    if diceOne > diceFour and diceTwo > diceFive:
        print('      Attacker: Lost 0 points')
    elif diceOne < diceFour and diceTwo > diceFive or diceOne > diceFour and diceTwo < diceFive:
        print('      Attacker: Lost 1 point')
    elif diceOne == diceFour and diceTwo > diceFive:
        print('      Attacker: Lost 1 point')
    elif diceOne == diceFour and diceTwo == diceFive:
        print('      Attacker: Lost 2 point')
    elif diceOne == diceFour and diceTwo < diceFive: 
        print('      Attacker: Lost 2 point')
    elif diceOne > diceFour and diceTwo == diceFive: 
        print('      Attacker: Lost 1 point')
    else:
        print('      Attacker: Lost 2 point')

    if diceFour >= diceOne and diceFive >= diceTwo:
        print('      Defender: Lost 0 point')
    elif diceFour >= diceOne and diceFive < diceTwo or diceFour < diceOne and diceFive > diceTwo:
        print('      Defender: Lost 1 point')
    else:
        print('      Attacker: Lost 2 point')

elif firstQuestion == 3 and secondQuestion == 1 or firstQuestion == 1 and secondQuestion == 3:

    print("Dice:")
    print('      Attacker: {0}-{1}-{2}'.format(diceOne,diceTwo,diceThree))
    print('      Defender: {0}\n'.format(diceFour))
    print("Outcome:")
   # if diceOne value is higher then attacker loses 0 points
    if diceOne > diceFour:
        print('      Attacker: Lost 0 points')
    else:
        print('      Attacker: Lost 1 point')
    
    # if diceFour is higher or equal to diceOne then defender loses 0 points
    if diceFour >= diceOne:
        print('      Defender: Lost 0 point')
    else:
        print('      Defender: Lost 1 point')

elif firstQuestion == 2 and secondQuestion == 2:
    print("Dice:")
    print('      Attacker: {0}-{1}'.format(diceOne,diceTwo))
    print('      Defender: {0}-{1}\n'.format(diceFour,diceFive))
    print("Outcome:")

    if diceOne > diceFour and diceTwo > diceFive:
        print('      Attacker: Lost 0 points')
    elif diceOne < diceFour and diceTwo > diceFive or diceOne > diceFour and diceTwo < diceFive:
        print('      Attacker: Lost 1 point')
    elif diceOne == diceFour and diceTwo > diceFive:
        print('      Attacker: Lost 1 point')
    elif diceOne == diceFour and diceTwo == diceFive:
        print('      Attacker: Lost 2 point')
    elif diceOne == diceFour and diceTwo < diceFive: 
        print('      Attacker: Lost 2 point')
    elif diceOne > diceFour and diceTwo == diceFive: 
        print('      Attacker: Lost 1 point')
    else:
        print('      Attacker: Lost 2 point')

    if diceFour >= diceOne and diceFive >= diceTwo:
        print('      Defender: Lost 0 point')
    elif diceFour >= diceOne and diceFive < diceTwo or diceFour < diceOne and diceFive > diceTwo:
        print('      Defender: Lost 1 point')
    else:
        print('      Attacker: Lost 2 point')

elif firstQuestion == 1 and secondQuestion == 2 or firstQuestion == 2 and secondQuestion == 1:

    print("Dice:")
    if firstQuestion == 1 and secondQuestion == 2:
        print('      Attacker: {0}'.format(diceOne))
        print('      Defender: {0}-{1}\n'.format(diceFour,diceFive))
    elif firstQuestion == 2 and secondQuestion == 1:
        print('      Attacker: {0},'.format(diceOne))
        print('      Defender: {0}-{1}\n'.format(diceFour,diceFive))        

    print("Outcome:")

    # if diceOne value is higher then attacker loses 0 points
    if diceOne > diceFour:
        print('      Attacker: Lost 0 points')
    else:
        print('      Attacker: Lost 1 point')
    
    # if diceFour is higher or equal to diceOne then defender loses 0 points
    if diceFour >= diceOne:
        print('      Defender: Lost 0 point')
    else:
        print('      Defender: Lost 1 point')





    

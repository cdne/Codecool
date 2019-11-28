import sys

# geetting number of arguments 
argumentsSize = len(sys.argv)

# list for all vowels
vowels = ['a', 'e', 'i', 'o', 'u']

# declaring string for lastLetter condition
lastLetter = ""

def testF():
    print("functie testF()")


# declaring function to check if the con - voc - con is true
# takes as parameter words added by user
def getLastThreeLetters(word):

    #declaring a boolean
    check = False

    # assigning in value as a lis last 3 letters
    value = list(word[-3:])
    
    # variable for while in function
    g = 0

    # executes 5 times
    while g < len(vocals):

        # if there is a consonant - vocal - consonant variable check becomes True
        if value[0] != vocals[g] and value[1] == vocals[g] and value[2] != vocals[g]:
            check = True 
        # counter g = g + 1  
        g += 1
    
    # returning True
    return check



# var for while
i = 1

# while executes until 1 is lower than the amount of words the user added
while i < argumentsSize:

    # each word the user adds is assigned to word variable
    word = sys.argv[i]
    
    # assigning the booleean from function
    checkedVocals = getLastThreeLetters(word)
    
    
   
    if word.endswith("e") and not word.endswith("ie"): 

        # delets the last letter and adds ing
        word = word[:-1] + "ing"
        print(word)

    
   
    elif word.endswith("ie"):

        # deletes the last 2 letters and adds ying
        word = word[:-2] + "ying" 
        print(word)

    # if the checkedVocals is True this elif is executeed
    elif checkedVocals:
        # assigns lastletter from word to variable
        lastLetter = word[-1:]
        
        # beg = begging
        word = word + lastLetter + "ing"
        print(word)
    else:
        word = word + "ing"
        print(word)

    # counter for while i = i + 1
    i += 1
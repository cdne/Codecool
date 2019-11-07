import sys

'''
Write an application that can save the given text into a local file. 
After saving the idea, it should show the existing ideas as well. 
The app should append the new idea into the file, to allow multiple ideas to be saved.
'''


listOfItems = []

def writeAndPrintValues():
    count = 0
    f = open("ideabank.txt", "r")
    print("\nYour ideabank:")
    for line in f:
        listOfItems.append(line.strip())
        print('{0}. {1}'.format(count+1, listOfItems[count]))
        count += 1
    f.close()


ideaBank = open("ideabank.txt", "a")

# Read user idea
idea = input("What is your new idea: ")
# writes the idea on file
ideaBank.write(idea)
ideaBank.write("\n")
# closes the file
ideaBank.close()

writeAndPrintValues()

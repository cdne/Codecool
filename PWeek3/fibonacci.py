'''
Write a script that prints out the first 30 numbers of
the Fibonacci sequence to the standard output.
'''

i = 0
j = 1
k = 0
fib = 0
getNumber = int(input("How many numbers do you want to output? "))
print("Fibonacci Sequance: ")
while(i < getNumber):
    print('{0}:                       {1}'.format(i + 1, fib))
    fib = j + k
    j = k
    k = fib
    i = i + 1
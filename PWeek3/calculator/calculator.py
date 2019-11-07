# declaring variables
number1, number2, result = 0, 0, 0
sign = ""

# informing the user what to do

info = '''

                                You will be asked to enter 2 numbers and a valid sign for operations

  If you enter a letter when you're asked for a number or anything else that is not a sign when asked for operation the app will stop


'''
print(info)

try:
  # read first number
  number1 = float(input("Enter first number: "))

  # read sign + - * /
  sign = input("Enter a sign (+ - * /): ")

  # if sign is not a sign except is executed and prints "Application stopped"
  if sign != "*" and sign != "-" and sign != "/" and sign != "+":
    sys.exit()
    

  # read second number
  number2 = float(input("Enter second number: "))
  
  
  # loop executes only if number1 or number2 are not strings
  while(number1 and number2) != "":
    if sign == "+":
      result = number1 + number2
      print("Result is: ", result)
    elif sign == "-":
      result = number1 - number2
      print("Result is: ", result)
    elif sign == "*":
      result = number1 * number2
      print("Result is: ", result)
    elif sign == "/":
      result = number1 / number2
      print("Result is: ", result)
    else:
      print("You didn't enter a valid sign")
     

    # after app executes if or elif, reads numbers and sign
    number1 = float(input("Enter first number: "))
    sign = input("Enter a sign (+ - * /): ")

      # if is not a sign applicaton stops with "Application stopped"
    if sign != "*" and sign != "-" and sign != "/" and sign != "+":
      sys.exit()
        
    number2 = float(input("Enter second number: "))
    
except:
  print("Application stopped")

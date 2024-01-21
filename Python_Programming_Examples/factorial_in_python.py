n= int(input("Enter a number: "))
fact =1
for i in range(1, n+1):
    fact = fact*i
print(fact)

def factorial(n):
  """This is a recursive function which
 calls itself to find the factorial of the given number """
  if n == 1:
    return n
  else:
    return n * factorial(n - 1)


# Asks the user to enter a number
n = int(input("Enter a number: "))
if n < 0:
  print("Factorial cannot be calculated for negative numbers!")
elif n == 0:
  print("Factorial of 0 is 1")
else:
  print("Factorial of", n, "is: ", factorial(n))


# Write a Python factorial program without using if-else, for, and ternary operators.

# import math
#
# #Defining the factorial() function to find factorial
# def factorial(num):
# 	return(math.factorial(num))
#
#
# # Input function to get the number from user
# num = int(input('Please enter a number to find the factorial: '))
#
# #Printing the factorial of the given number
# print("The factorial of the given number", num, "is",
# 	factorial(num))
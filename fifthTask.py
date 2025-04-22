import math

from helper import is_number

user_input = input("Enter a positive integer N: ")

if is_number(user_input) and float(user_input).is_integer() and int(user_input) > 0:
    N = int(user_input)
    n = N + 5
    print(f"Factorial of {n} is: {math.factorial(n)}")
else:
    print("Invalid input. Please enter a positive integer.")
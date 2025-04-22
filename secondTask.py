import math

from helper import is_number

print("Hello. Please, enter specific numbers to calculate the Y expression!")

x_input = input("Enter value for x: ")
a_input = input("Enter value for a: ")

if is_number(x_input) and is_number(a_input):
    x = float(x_input)
    a = float(a_input)

    if x <= -1:
        y = a * math.cos(x + 1) + a
    else:
        y = (a * (x + 2) ** 3) / 2

    print(f"Calculated value of Y: {y}")
else:
    print("Error: You must enter valid numeric values for x and a.")

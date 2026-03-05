# Task 6: Using the Math Module for Calculations
# Problem Statement: Write a Python program that:
# 1.Asks the user for a number as input.
# 2.Uses the math module to calculate the:


import math

usr_input = int(input("Enter the number: "))


square_root = math.sqrt(usr_input)

print(f"Square root of {usr_input} is: {square_root}")


logarithm = math.log(usr_input)

print(f"Logarithm of {usr_input} is: {logarithm}")


sine = math.sin(usr_input)

print(f"Sine of {usr_input} is: {sine}")


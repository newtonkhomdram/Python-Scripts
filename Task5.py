# Task 5: Calculate Factorial Using a Function 
# Problem Statement: Write a Python program that:
# 1.Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
# 2.Returns the calculated factorial.
# 3.Calls the function with a sample number and prints the output.


def fact(num):

    if num == 1:

        return 1

    else:

        factorial = num * fact(num - 1)

        return factorial

usr_input = int(input("Enter the number: "))

print(f"Factorial of {usr_input} is: {fact(usr_input)}")
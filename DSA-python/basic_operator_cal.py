"""
Create a program that takes two numbers and a math operator (+, -, *, /) from the user, performs the corresponding calculation, and prints the result.

Sample Input: num1=15, num2=3, operator='/'
Sample Output: Result: 5.0

"""

import math

def main():
    num1 = int(input("Enter a 1st number: "))
    num2 = int(input("Enter a 2nd number: "))
    opr = input("enter operator('+', '-', '*', '/'): ")

    if opr == "+":
        result = num1 + num2
    elif opr == "-":
        result = num1 - num2
    elif opr == "*":
        result = num1 * num2
    elif opr == "/":
        result = num1 / num2
    else:
        result = "invalid operator"

    print("Result: ", result )





main()
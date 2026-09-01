
"""
find the factorial of a number
"""

def main():
    number = int(input("Enter number: "))

    i = 1
    fact = 1

    while i <= number:
        fact = fact * i
        i += 1

    print(number, fact)

main()
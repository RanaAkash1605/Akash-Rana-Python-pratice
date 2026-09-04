"""
Write a program that takes an integer from the user and prints its multiplication table from 1 to 10.

Sample Input: 5
Sample Output:
5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50
"""

def main():
    n = int(input("Enter the number: "))

    for i in range(1, 11):
        print(f"{n} X {i} =", n*i)


main()
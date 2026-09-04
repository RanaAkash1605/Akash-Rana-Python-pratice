"""
Write a Python script to print the first 
N
 terms of the Fibonacci sequence, where 
N
 is provided by the user.

Fibonacci sequence: 0 1 1 2 3 5 8 13 21

Sample Input: N = 6

Sample Output: 0, 1, 1, 2, 3, 5
"""


def main():
    n = int(input("Enter a number: "))

    first_num = 0
    second_num = 1

    for _ in range(n):
        print(first_num, end=" ")
        first_num, second_num = second_num, first_num + second_num

main()
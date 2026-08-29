"""
Write a script that accepts a positive integer N
from the user and calculates the sum of all natural numbers up to N.

Sample Input: N = 10
Sample Output: Sum: 55


"""

def main():
    num = int(input("Enter a number: "))
    total_sum = (num * (num + 1)) // 2
    print("Sum:", total_sum)


main()
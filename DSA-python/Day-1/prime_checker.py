"""
Write a program that checks whether a positive integer entered by the user is a prime number.
Logic: A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.

Sample Input: 17
Sample Output: 17 is a prime number.
"""
def main():
    num = int(input("Enter a number: "))
  
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(f"{num} is not a prime number")
            break
        else:
            print(f"{num} is a prime number")
            break



main()
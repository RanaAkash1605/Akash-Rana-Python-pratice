"""
Write a program that takes a string input from the user, reverses the string, converts the entire reversed string to uppercase, and prints the result.

Sample Input: "Bangalore"
Sample Output: "EROLAGNAB"
"""

str = input("Enter string: ")

x = str.upper()
reversed_str = x[::-1] # starts from end -ve indexing

print(reversed_str)
"""
Write a program that prompts the user for a text string and a shift integer, and encrypts the text using a Caesar cipher. 
It should shift each alphabetical character in the string by the specified shift number down the alphabet. 
Maintain uppercase and lowercase characters, and leave spaces or punctuation marks completely unchanged.

Sample Input: (User inputs string "Vinod" and shift 3)
Sample Output: "Ylqrg"
"""

text = input("Enter string: ")
shift = int(input("Enter shift: "))

result = ""

for letter in text:

    if 'A' <= letter <= 'Z':
        result += chr((ord(letter) - ord('A') + shift) % 26 + ord('A'))

    elif 'a' <= letter <= 'z':
        result += chr((ord(letter) - ord('a') + shift) % 26 + ord('a'))

    else:
        result += letter

print(result)
     
    


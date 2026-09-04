"""
Write a program that accepts a string input from the user and outputs it in Title Case 
(capitalizing the first letter of each word and 
lowercasing the remaining letters). Do not use Python's built-in .title() method.

Sample Input: "WELCOME TO BANGALORE CITY"
Sample Output: "Welcome To Bangalore City"

"""

sentence = input("Enter a sentence: ")

words = sentence.split()

result = []

for word in words:
    first_letter = word[0].upper()
    remaining_letters = word[1:].lower()

    new_word = first_letter + remaining_letters

    result.append(new_word)

final_sentence = " ".join(result)

print(final_sentence)

        



"""
Write a Python program that prompts the user to enter a sentence. The program must count and display:
The total number of characters (including spaces and punctuation).
The total number of words.

Sample Input: "Learning Python is fun!"
Sample Output:
Total Characters: 23
Total Words: 4
"""
def main():
    sentence = input("Enter Sentence : ")

    total_characters = len(sentence)
    total_words = len(sentence.split())

    print(total_characters)
    print(total_words)

main()
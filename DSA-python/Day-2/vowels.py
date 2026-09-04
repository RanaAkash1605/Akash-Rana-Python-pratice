"""
Write a program that prompts the user to enter a string and counts:
The individual frequency of each vowel (a, e, i, o, u), case-insensitively.
The total count of all consonants.

Sample Input: "Vinod Kumar Kayartaya"
Sample Output:
Vowel Frequencies:
a: 4
e: 0
i: 1
o: 1
u: 1
Total Consonants: 12
"""

text = input("Enter a string: ").lower()

vowels = "aeiou"

for vowel in vowels:
    print(vowel + ":", text.count(vowel))

consonants = sum(1 for char in text if char.isalpha() and char not in vowels)

print("Total Consonants:", consonants)



"""
Write a program that prompts the user to enter a full name (first name, middle name, last name) and anonymizes it.
 The output should print the initials of the first and middle names followed by the full last name. 
 If the name consists of only a single word, print it as-is.

Sample Input: "Vinod Kumar Kayartaya"
Sample Output: "V. K. Kayartaya"
Sample Input: "Bangalore"
Sample Output: "Bangalore"
"""

name = input("Enter Name : ")
full_name = name.split()


if len(name) == 1 :
    print(full_name[0])

else:
    out = ""
    for i in range(len(full_name) - 1):
        out += full_name[i][0].upper() + "."

out += full_name[-1]
print(out)
    
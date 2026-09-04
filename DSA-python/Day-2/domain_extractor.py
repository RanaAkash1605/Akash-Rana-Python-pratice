"""
Write a program that prompts the user to enter an email address string. Extract the domain name (the part after the @) and
print it. If the string is not a valid email (does not contain exactly one @), print "Invalid Email".

Sample Input: "vinod@vinod.co"
Sample Output: "vinod.co"
Sample Input: "vinod.co"
Sample Output: "Invalid Email"
"""


email = input("Enter email: ")

if "@" not in email:
    print("invalid email")

else:
    x = email.find("@") # retrun the lowest index value
    y = email[x+1 :]
    print(y)
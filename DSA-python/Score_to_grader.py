"""
Write a script that takes a numeric test score from the user (0 to 100) and displays a corresponding letter grade based on the following scale:

90-100: A
80-89: B
70-79: C
60-69: D
Below 60: F
"""
def main():
    num = int(input("Enter a score: "))

    if 90 <= num <= 100:
        print("Grade : A")
    elif 80 <= num <= 89:
        print("Grade : B")
    elif 70 <= num <= 79:
        print("Grade : C")
    elif 60 <= num <= 69:
        print("Grade : D")
    elif 0 < num < 60:
        print("Grade: F")
    else:
        print("Invalid Number")

print("Grade: ")

print("="* 100)    

main()
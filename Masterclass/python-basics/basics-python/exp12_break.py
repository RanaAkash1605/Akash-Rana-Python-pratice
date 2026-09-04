"""
Break statement
"""

def main():

    while True:
        choice = input("Enter 'q' to quit, any other key to continue: ") # it takes capital Q as well

        if choice.lower() == 'q':
            print("Exitting loop")
            break
        print("running process")
    print("Porgram continues here: ") 

main()
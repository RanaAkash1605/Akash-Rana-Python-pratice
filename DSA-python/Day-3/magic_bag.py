"""
Scenario: A wizard has a magic bag containing a sequence of items: ["staff", "potion", "spellbook"]. When the wizard steps through a magic portal, two things happen:
A new item enters the bag (prompts the user to input the item name to append to the end).
The oldest item in the bag (at index 0) is dissolved and ejected. Write a program to simulate this portal transition and 
print the final bag contents.

Sample Input: (User inputs "amulet")

Sample Output:

Portal transition activated!
Ejected oldest item: staff
Current items in the magic bag: ['potion', 'spellbook', 'amulet']

"""

def main():

    magic_bag = ["staff", "potion", "spellbook"]

    add_item = input("Enter the new item: ")

    x = magic_bag[0]
    magic_bag.remove(x)

    print("Portal transition activated!")
    print(f"Ejected olest item : {x}")

    magic_bag.append(add_item)  

    print(f"Current items in the magic bag: {magic_bag}")


main()
def main():
    age = int(input("what's your age? :"))

    if age < 18:
        print(f"you cannot vote right now, wait for {18-age} years")
    else:
        print("you can and should vote")
main()        
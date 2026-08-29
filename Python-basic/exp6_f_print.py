def main():
    name = input("what's your name: ")
    city = input('Where are from?: ')

    print(f"hello {name}, how's weather in {city}?")

    age = int(input('How old are you: '))

    print(f"OK, so you are {age} years old!")
    future_age = age + 10
    print(f"After 10 years you are {future_age} years old!")

main()
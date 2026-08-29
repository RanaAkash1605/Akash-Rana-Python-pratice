def main():
    name = input("what's your name?: ")
    city = input("where are you from?: ")

    if name.strip() == "":
        name = "friend"

    if len(city.strip()) == 0:
        city = "your city"

        print(f"hello {name}, how's weather in {city}?")
main()        

# strip is used to remove the whitespaces
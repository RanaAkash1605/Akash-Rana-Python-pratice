def main():
    year = int(input('Enter year: '))
    month = int(input("Enter month: "))

    if year < 1:
       print(f"Invalid value for month: {year}")
       return

    if month < 1:
        print(f"Invalid value for month: {year}")
        return

    if month == 2:
        max_days = 29 if year % 400 == 0 or year % 4 == 0 or year % 100 != 0 else 28
    elif month in (4,6,9,11):
          max_days = 30
    else:
     max_days = 31

    print(f"{month}/{year} has {max_days} days")
main()    
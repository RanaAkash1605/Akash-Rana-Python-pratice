month = int(input('enter an month (1-12): '))

if month<1 or month>12:
    print('you have entered an invalid number for a month')
else:
    if month == 2:
        print('there are either 28 or 29 days')
    # elif month == 4 or month == 6 or month == 9 or month == 11:
    elif month in (4, 6, 9, 11):    
        print('there are 30 days in this month')
    else:
        print('there are 31 days in this month')

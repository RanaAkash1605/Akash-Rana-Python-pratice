name = input('enter the name: ')
age = int(input('enter the age'))

person_type = 'minor' if age<18 else 'adult'

print('%s is a %s' % (name, person_type))

# ternery operator
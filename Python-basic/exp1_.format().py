name = input("enter your name : ")
city = input("enter your city : ")

# print('hello', name, 'how are you?')
# print('hello %s, how are you?' % name)
# print('hello %s, how is wheather in %s?' % (name, city))
msg = 'hello {}, how is wheather in {}?'.format(name,city)
print(msg) 

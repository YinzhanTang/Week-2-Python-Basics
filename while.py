Name = input('Your name is ? ')
test = Name[0]. islower()
while test is True:
    print('Error.Must be capitalized.')
    Name = input('Input your name again: ')
    test = Name[0]. islower()

else:
    print('Hello, '+ Name)

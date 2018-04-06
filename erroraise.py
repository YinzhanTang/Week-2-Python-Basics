price = int(input('Price: '))
while price <= 0:
    print ('Declined.Price must be non negative')
    price = int(input('Please input again: '))

print ('price accepted ')

population = int(input('Population: '))
while population <= 0:
    raise ValuError ('Declined.Population must be non negative')

print ('population accepted')

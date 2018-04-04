x = int(input('What is the value of x ?'))

if ( x < 0 ):
    print('x is negative')
elif ( x == 0):
    print('x is zero')
else:
    print('x is positive')

if ( x % 2 == 0 ):
    print('x is even')
else:
    print('x is odd')

print('Is x both negative and even? '+ str(x < 0 and x % 2 == 0))

print('Is x negative or even? ', x < 0 or x % 2 == 0)

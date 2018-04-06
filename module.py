import math

def sequence(n):
    while n > 0:
          print(n)
          n = n - 1
    print ('Blastoff!')

def quadratic(a,b,c):

    if a == 0:
        raise ValuError ('a cannot be zero')
    else:
        if b**2 - 4*a*c < 0:
            print ('The equation has no solution')

        if b**2 - 4*a*c >= 0:
            x1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
            x2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
            return (x1,x2)

a = float(input('input a :'))
b = float(input('input b :'))
c = float(input('input c :'))
print(quadratic(a,b,c))

import math

def distance(x1,y1,x2,y2):
    dx = x2 -x1
    dy = y2 -y1

    dsquared = dx**2 + dy**2
    print('dsquared is ', dsquared)
    return math.sqrt(dsquared)

x1 = int(input('Input x1 = '))
x2 = int(input('Input x2 = '))
y1 = int(input('Input y1 = '))
y2 = int(input('Input y2 = '))

distance = int(distance(x1,y1,x2,y2))
print('distance is ', distance)

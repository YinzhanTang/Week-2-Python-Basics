import math

distance(x1,y1,x2,y2):
    dx = str(x2 -x1)
    dy = y2 -y1

    print('dx is '+ dx) #此处表现形式两种皆可, +只能接string
    print('dy is', dy) # ，后面接的是intergal

    return 0.0

x1 = int(input('Input x1 = '))
x2 = int(input('Input x2 = '))
y1 = int(input('Input y1 = '))
y2 = int(input('Input y2 = '))

distance(x1,y1,x2,y2)

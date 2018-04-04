import math

def hypotenuse(a,b):
    return math.sqrt(a**2 + b**2)
a = int(input ('What is the value of a ? '))
b = int(input ('What is the value of b ? '))
result = int(hypotenuse(a,b))
print(result)

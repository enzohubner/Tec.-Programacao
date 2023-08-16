import math
z = float (input("digite o valor d z: "))
w = float (input("digite o valor d w: "))

if w>0 or  z<7:
    x = (5*w + 1)/3
    t = 5*z+2
else:
    t = (5*w + 1)/3
    x = 5*z+2        

raizX = math.sqrt(x)
cuboX = x*x*x

y = 7*cuboX -3*raizX -8*t/ 5*x + 5
print(y)
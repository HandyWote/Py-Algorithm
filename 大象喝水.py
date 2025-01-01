import math
h,r = map(int,input().split())
V = 20
v = (3.14*r*r*h)/1000
V/v
print(math.ceil(V/v))
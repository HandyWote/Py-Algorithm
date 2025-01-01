import math
n = int(input())
f1 = pow((1+math.sqrt(5))/2,n)
f2 = pow((1-math.sqrt(5))/2,n)
f = (f1 - f2)/math.sqrt(5)
print("%.2f"%f)
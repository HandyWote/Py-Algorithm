import math
x = int(input())
if x < 60:
    x = math.floor(pow(x,0.5)*10)
    if x < 60:
        gpa = 0.0
if x >= 90:
    gpa = 4.0
if 60 <= x < 90:
    gpa = 4.0 - 0.1*(90-x)
print("%.1f"%gpa)
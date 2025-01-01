import math

def cantor(n):
    a = (math.sqrt(8*n - 7) + 1) // 2
    b = n - (a * (a - 1) // 2)
    if a % 2:
        num, den = a - b + 1, b
    else:
        num, den = b, a - b + 1
    return f"{int(num)}/{int(den)}"
n = int(input())
print(cantor(n))
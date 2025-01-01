import math
from decimal import Decimal
c = int(input())
for a in range(1, int(math.sqrt(c * c)) + 1):
    b = math.sqrt(c * c - a * a)
    if b.is_integer() and a <= b:
        print(a, int(b))
        break
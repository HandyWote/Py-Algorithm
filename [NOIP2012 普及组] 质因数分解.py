import math
n = int(input())
if n == 2:
    print(2)
else:
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0 :
            print(n//i)
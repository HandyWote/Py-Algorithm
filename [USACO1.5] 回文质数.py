a,b = map(int,input().split())
for i in range(a, b):
    qi = int(i**0.5)
    if i % 2 != 0 or i % 3 != 0:
        if all(i%j!=0 for j in range(2, qi + 1)) and str(i) == str(i)[::-1]:
            print(i)
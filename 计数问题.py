a,b = map(int,input().split())
n = 0
b = str(b)
for i in range (1,a+1):
    j =str(i)
    n += j.count(b)
print(n)
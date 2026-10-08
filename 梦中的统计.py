from collections import Counter
m,n = map(int,input().split())
a = ''.join([str(i) for i in range (m,n+1)])
b = Counter(a)
print(" ".join([str(b[str(i)]) for i in range(10)]))
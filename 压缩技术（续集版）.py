a = input()
n = len(a)
count = 0
u = 1
for i in range(1,n):
    a += input()
print(n,end=' ')
for i in range(len(a)):
    if u == 1:
        if a[i] != 1:
            count += 1
        
print('')
a = []
for i in range(7):
    a.append(sum(list(map(int,input().split()))))
if max(a) > 8:
    print(a.index(max(a))+1)
else:
    print(0)
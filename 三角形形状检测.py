l = input().split()
a,b,c = map(int,l)
l = [int(k) for k in l]
u = [int(k) for k in l]
m = max(l)
l.remove(max(l))
if sum(l)<=m:
    print('Not triangle')
else:
    #形状
    square = list(map(lambda x:x**2,u))
    ms = max(square)
    square.remove(max(square))
    if sum(square)>ms:
        print('Acute triangle')
    if sum(square)==ms:
        print('Right triangle')
    if sum(square)<ms:
        print('Obtuse triangle')
    #等腰，等边
    if a == b or a == c or b == c:
        print('Isosceles triangle')
    if a == b == c:
        print('Equilateral triangle')
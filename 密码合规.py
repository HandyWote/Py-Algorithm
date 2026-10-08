key = [str(i) for i in input().split(',')]
b = 'abcdefghijklmnopqrstuvwxyz'
B = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n = '1234567890'
k = '!@#$'
all = b + B + n + k
key1 = []
for i in key:
    remove = 0
    a1,a2,a3,a4 = 0,0,0,0
    for j in i:
        if not j in all:
            remove += 1
        #条件二
        if j in b:
            a1 = 1
        if j in B:
            a2 = 1
        if j in n:
            a3 = 1
        if j in k:
            a4 = 1

    #条件三
    if not 6<=len(i)<=12:
        remove += 1

    if not (a1+a2+a3>=2 and a4 == 1):
        remove += 1

    if remove == 0:
        key1.append(i)

for i in key1:
    print(i)
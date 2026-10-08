l = int(input())
s = 0
a = []
if l == 2:
    print(1)
else:
    for i in range(2, l):
        if all(i%j!=0 for j in range(2, int(i**0.5)+1)):
            a.append(i)
            if sum(a) > l:
                break
            print(i)
            s += 1
    print(s)
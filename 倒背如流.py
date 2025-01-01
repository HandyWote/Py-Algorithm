a = input().split()
a = [int(x) for x in a]
a.remove(0)
a.reverse()
a =  [str(i) for i in a]
a = " ".join(a)
print(a)
a, b, c = map(int,sorted(list(map(int, input().split()))))
d = {
    'A': a,
    'B': b,
    'C': c
}
l = input()
print("%d %d %d" % (d[l[0]], d[l[1]], d[l[2]]))
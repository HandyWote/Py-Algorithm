a = input().split()
a = list(map(int,a))
a.sort(reverse=False)
print(*a)
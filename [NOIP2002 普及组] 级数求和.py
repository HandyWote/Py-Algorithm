k = int(input())
s = 0
i = 1
while 1:
    s += 1/i
    if s > k:
        print(i)
        break
    i += 1
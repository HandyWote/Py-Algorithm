a = int(input())
b = int(input())
i = 0
while i < a:
    i += 1
    if i % b == 0:
        continue
    else:
        print (i)
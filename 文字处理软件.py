q = int(input())
strr = input().strip()
b = [strr]

for _ in range(q):
    m = input().split()
    if m[0] == '1':
        b.append(b[-1] + m[1])
        print(b[-1])

    elif m[0] == '2':
        start, length = int(m[1]), int(m[2])
        b.append(b[-1][start:start+length])
        print(b[-1])

    elif m[0] == '3':
        start = int(m[1])
        b.append(b[-1][:start] + m[2] + b[-1][start:])
        print(b[-1])

    elif m[0] == '4':
        print(b[-1].find(m[1]))
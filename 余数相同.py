l = map(int,input().split())
l = [int(k) for k in l]
a,b,c = map(int,l)
answer = []
for i in range(max(l)):
    ay = a % (i+2)
    by = b % (i+2)
    cy = c % (i+2)
    if ay == by == cy:
        answer.append(i+2)
print(min(answer))
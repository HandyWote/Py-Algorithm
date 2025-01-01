n = int(input())
heat = []
while n != 1:
    for k in range(2,n+1):
        if n % k == 0:
            heat.append(k)
            n = n // k
            break
print(sum(heat))
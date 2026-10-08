s = float(input())
step = 0
strenth = 2
while s > 0:
    s -= strenth
    strenth *= 0.98
    step += 1
print(step)
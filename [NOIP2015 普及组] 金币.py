k = int(input())
gold = 0
prize = 1
day = 0
for i in range(1,k+1):
    for j in range(i):
        if day >= k:
            break
        day += 1
        gold += prize
    prize += 1 
print(gold)
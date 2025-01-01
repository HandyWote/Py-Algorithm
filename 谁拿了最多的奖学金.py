n = int(input())
name = []
almoney = []
for _ in range (n):
    imfor = input().split()
    name.append(imfor[0])
    money = 0
    if int(imfor[1]) > 80 and int(imfor[5]) > 0:
        money += 8000
    if int(imfor[1]) > 85 and int(imfor[2]) > 80:
        money += 4000
    if int(imfor[1]) > 90:
        money += 2000
    if int(imfor[1]) >85 and imfor[4] == "Y":
        money += 1000
    if int(imfor[2]) > 80 and imfor[3] == "Y":
        money += 850
    almoney.append(money)
print(name[almoney.index(max(almoney))])
print(max(almoney))
print(sum(almoney))
lucky = int(input())
l = int(input())
r = int(input())
bag = []
d = r - l + 1
for i in range (0,d):
    key =  i+l
    if key % lucky == 0:
        bag.append(key)
    if str(lucky) == str(key)[-1]:
        bag.append(key)
bag = list(set(bag))
s = sum(bag)
print(s)
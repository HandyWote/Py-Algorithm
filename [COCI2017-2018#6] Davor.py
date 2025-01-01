money = int(input())
mw = (money / 52) / 7
for k in range(1,int(mw)+1):
    x = mw - 3 * k
    if 100 >= x >= 1 and x % 1 == 0:
        print(int(x))
        print(k)
        break
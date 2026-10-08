y,m = map(int,input().split())
bigmonth = [1,3,5,7,8,10,12]
small = [4,6,9,11]
if m in  bigmonth:
    print(31)
if m in small:
    print(30)
if m  == 2:
    if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
        print(29)
    else:
        print(28)
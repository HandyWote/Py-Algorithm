h1,m1,h2,m2 = map(int,input().split())
a1 = h1 * 60 + m1
a2 = h2 * 60 + m2
print("%d %d" % ((a2-a1)//60 , int((a2-a1)%60)))
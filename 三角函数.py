a,b,c = map(int,input().split())
def g(x,y):
    if y == 0:
        return x
    else:
        return g(y,x%y)
g1 = g(min(a,b,c),max(a,b,c))
print("%d/%d" % (min(a,b,c)//g1,max(a,b,c)//g1))
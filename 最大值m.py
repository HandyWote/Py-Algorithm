a,b,c = map(int,input().split())
m = max(a,b,c)/(max(a+b,b,c)*max(a,b,b+c))
print("%.3f"%m)
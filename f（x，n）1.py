def f(x,n):
    for i in range(1,n+1):
        x = pow(i + x,0.5)
    return float(x)
x,n = input().split()
print("%.2f"%f(float(x),int(n)))
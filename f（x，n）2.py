def f(x,n):
    if n == 1:
        return x / (x + 1)
    else:
        return x / (n + f(x,n-1))
x = float(input())
n = int(input())
print("%.2f" % f(x,n)),
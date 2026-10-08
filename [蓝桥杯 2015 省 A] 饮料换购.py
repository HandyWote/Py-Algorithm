n = int(input())
def check(n):
    ans = 0
    if n < 3:
        return ans
    m = n%3
    n = (n-m)//3
    ans += n
    ans += check(n+m)
    return ans
ans = check(n)+n
print(ans)
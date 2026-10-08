t = int(input())
def get(s1):
    n = len(s1)
    d = 0
    h, m, s = map(int, s1[0].split(':'))
    t1 = h*3600+m*60+s
    h, m, s = map(int, s1[1].split(':'))
    t2 = h*3600+m*60+s
    if n>=3:
        d = int(''.join(filter(str.isdigit, s1[2])))
    return t2+d*24*3600 - t1
for _ in range(t):
    s1 = input().split()
    t1 = get(s1)
    s2 = input().split()
    t2 = get(s2)
    ans = (t1+t2)//2
    h = ans//3600
    m = ans%3600//60
    s = ans%3600%60
    print(f'{h:02}:{m:02}:{s:02}')
    
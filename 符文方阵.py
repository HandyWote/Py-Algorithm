
def main():
    n, m, mitrixs = get_input()
    q = mitrixs.pop()
    while mitrixs:
        p = mitrixs.pop()
        q = f(m, p, q)
    print_mitrix(m, q)
    
def get_input():
    n, m = map(int, input().split())
    mitrix = []
    a = []
    for i in range(1, n*m+1):
        for x in input().split():
            a.append(int(x))
        if i % m == 0:
            mitrix.append(a)
            a = []
    return n, m, mitrix

def f(m, p, q):
    s_m = m**2
    c = [0] * s_m
    for x in range(s_m):
        j = x % m
        i = x - j
        for k in range(m):
            c[x] += (p[i+k]*q[m*k+j]) % 2
        c[x] %= 2
    return c

def print_mitrix(m,q):
    for i in range(m):
        print(*q[i*m:(i+1)*m])


if __name__ == '__main__':
    main()
import sys, math
input = lambda: sys.stdin.readline()

def main():
    n = int(input())
    a = list(map(int, input().split()))
    # 获取最小公倍数
    lcm = 1
    for i in range(n):
        lcm = lcm * a[i] // math.gcd(lcm, a[i])
    print(lcm%998244353)


if __name__ == '__main__':
    main()
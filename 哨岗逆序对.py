import sys
input = sys.stdin.readline

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if a[i] > a[j]: ans += 1
    print(ans%100)

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    hs = [0]*(max(a)+1)
    for i in a:
        ans += sum(hs[i+1:])
        hs[i] += 1
    print(ans%100)

if __name__ == '__main__':
    main()
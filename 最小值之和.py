
def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        x = a[i]
        for j in range(i, n):
            x = min(x, a[j])
            ans += x
    print(ans)


if __name__ == '__main__':
    main();
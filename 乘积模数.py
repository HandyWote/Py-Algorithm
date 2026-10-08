
def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 1
    for i in a:
        ans = ans * i % 998244353
    print(ans % 998244353)


if __name__ == '__main__':
    main();
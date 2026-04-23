
def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in a:
        if i < k:
            ans += (i+1)*i//2
            k -= i
        else:
            ans += (2*i-k+1)*k//2
            break
    print(ans)


if __name__ == '__main__':
    main()
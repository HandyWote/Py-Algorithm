
def main():
    n = int(input())
    ans = 0
    for x in input().split():
        for i in x:
            ans += int(i)
    print(ans)

if __name__ == '__main__':
    main();
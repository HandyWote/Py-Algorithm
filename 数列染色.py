
def get_input():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    return n, k, a

if __name__ == '__main__':
    n, k, a = get_input()
    ans = a[0]+a[-1]
    a = a[1:-1]
    
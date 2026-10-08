def get_input():
    n = int(input())
    a = list(map(int, input().split()))
    return n, a

if __name__ == "__main__":
    n, a = get_input()
    a.sort()
    print(*a)
    print(*a[::-1])
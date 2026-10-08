import sys
input = sys.stdin.readline

def solve(n):
    return 2 * n if n % 3 == 0 else n

t = int(input())
for _ in range(t):
    print(solve(int(input())))
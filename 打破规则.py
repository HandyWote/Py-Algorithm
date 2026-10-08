import sys
input = sys.stdin.readline
a, b, c = map(int, input().split())
if a >= b >= c or c >= b >= a:
    print(0)
    sys.exit()
print(min(abs(a-b), abs(a-c), abs(b-c)))
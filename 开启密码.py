import sys
input = sys.stdin.readline

from collections import Counter

def main():
    n = int(input())
    a = Counter(map(int, input().split()))
    b = sorted(a.items(), key=lambda x: (-x[-1], x[0]))
    for i in b:
        if i[-1] == b[0][-1]: print(i[0])
        else: break

if __name__ == '__main__':
    main()
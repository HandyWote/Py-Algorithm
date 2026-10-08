import sys
input=lambda:sys.stdin.readline()
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        ans = sum(x for x in a[1:] if x >= 0)
        print(ans)
        
if __name__ == '__main__':
    main();
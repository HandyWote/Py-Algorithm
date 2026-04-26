import sys
input = sys.stdin.readline

def main():
    s = input()
    ans = set()
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            ans.add(s[i:j])
    print(len(ans))

if __name__ == '__main__':
    main()
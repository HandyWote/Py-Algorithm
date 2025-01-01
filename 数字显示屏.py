cal = [
    '****.**.**.****',
    '..*..*..*..*..*',
    '***..*****..***',
    '***..****..****',
    '*.**.****..*..*',
    '****..***..****',
    '****..****.****',
    '***..*..*..*..*',
    '****.*****.****',
    '****.****..****'
]

def main():
    n = int(input())
    s = []
    for _ in range(5):
        s.append(input())
    l = 0
    while l < n * 4 - 1:
        t = ""
        for i in range(5):
            for j in range(l, l + 3):
                t += s[i][j]
        for i in range(10):
            if t == cal[i]:
                print(i, end='')
                break
        l += 4
    print()

main()
def main():
    n = int(input())
    a = list(map(int, input().split()))
    pos, neg = function(a)
    print(pos, neg)

def function(a):
    pos, neg = 0, 0
    for i in a:
        if i > 0:
            pos += 1
        elif i < 0:
            neg += 1
    return pos, neg

if __name__ == '__main__':
    main()
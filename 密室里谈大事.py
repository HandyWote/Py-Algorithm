def main():
    n = int(input())
    a = list(map(int, input().split()))
    
    print(*function(a))

def function(a):
    bad, not_bad, good, excilent = 0, 0, 0, 0
    for i in a:
        if i < 60:
            bad += 1
        elif 60 <= i <= 79:
            not_bad += 1
        elif 80 <= i <= 89:
            good += 1
        else:
            excilent += 1
    return bad, not_bad, good, excilent

if __name__ == '__main__':
    main()
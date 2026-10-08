import sys

def main():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    for _ in range(t):
        n = int(input[ptr])
        ptr += 1
        a = list(map(int, input[ptr:ptr+n]))
        ptr += n
        b = list(map(int, input[ptr:ptr+n]))
        ptr += n
        
        c = a.copy()
        d = b.copy()
        c.sort()
        d.sort()
        
        flag = False
        for i in range(n):
            if c[i] != d[i]:
                flag = True
                break
        
        if flag:
            print("NO")
            continue
        
        print("YES")
        a_current = a.copy()
        for i in range(n):
            target = b[i]
            num = a_current.index(target)
            for j in range(num, i, -1):
                print(j+1, j)
                a_current[j], a_current[j-1] = a_current[j-1], a_current[j]
        print("0 0")

if __name__ == "__main__":
    main()
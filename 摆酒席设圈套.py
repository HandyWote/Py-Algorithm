MOD = 10007

def get_intput():
    n = int(input())
    a = list(map(int, input().split()))
    return n, a

def pre_less(n: int, a: list):
    # 预处理less_left
    less_left = [0] * n
    for i in range(n):
        cnt = 0
        for j in range(i):
            if a[j] < a[i]:
                cnt += 1
        less_left[i] = cnt
    # 预处理less_right
    less_right = [0] * n
    for i in range(n):
        cnt = 0
        for j in range(i + 1, n):
            if a[j] < a[i]:
                cnt += 1
        less_right[i] = cnt
    return less_left, less_right
    
def get_ans(n: int, a: list, less_left: list, less_right: list):
    ans = 0
    # 枚举所有w < e 且值相等的对
    for w in range(n):
        for e in range(w + 1, n):
            if a[w] == a[e]:
                ans = (ans + less_left[w] * less_right[e]) % MOD
    return ans

def main():
    n, a = get_intput()
    l, r = pre_less(n, a)
    print(get_ans(n, a, l, r))

if __name__ == "__main__":
    main()
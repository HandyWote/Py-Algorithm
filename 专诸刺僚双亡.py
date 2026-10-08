import sys
input = sys.stdin.readline

def get_input():
    _, q_num = map(int, input().split())
    a = list(map(int, input().split()))
    q = []
    for i in range(q_num):
        l, r = map(lambda x: int(x) - 1, input().split())
        q.append([l, r, i])
    return q, a

def solve(a: list, q: list):
    # 莫队: 离线排序查询, 滑动窗口维护区间众数次数
    n = len(a)
    block = int(n ** 0.5) + 1
    # 按左端点所在块排序, 块内右端点单调(之字形减少指针回头)
    q.sort(key=lambda x: (x[0] // block, x[1] if (x[0] // block) % 2 == 0 else -x[1]))

    cnt = [0] * (max(a) + 1)  # 窗口内每个值的出现次数
    freq = [0] * (n + 1)      # 出现次数为 c 的值有多少个
    freq[0] = max(a) + 1
    most_cnt = 0
    ans = [0] * len(q)
    cl, cr = 0, -1            # 当前窗口, 初始为空

    for l, r, i in q:
        while cr < r:  # 右端伸长
            cr += 1
            v = a[cr]
            c = cnt[v]
            cnt[v] = c + 1
            freq[c] -= 1
            freq[c + 1] += 1
            if c + 1 > most_cnt:
                most_cnt = c + 1
        while cl > l:  # 左端伸长
            cl -= 1
            v = a[cl]
            c = cnt[v]
            cnt[v] = c + 1
            freq[c] -= 1
            freq[c + 1] += 1
            if c + 1 > most_cnt:
                most_cnt = c + 1
        while cr > r:  # 右端收缩
            v = a[cr]
            c = cnt[v]
            cnt[v] = c - 1
            freq[c] -= 1
            freq[c - 1] += 1
            if freq[most_cnt] == 0:
                most_cnt -= 1
            cr -= 1
        while cl < l:  # 左端收缩
            v = a[cl]
            c = cnt[v]
            cnt[v] = c - 1
            freq[c] -= 1
            freq[c - 1] += 1
            if freq[most_cnt] == 0:
                most_cnt -= 1
            cl += 1
        ans[i] = most_cnt
    return ans

def main():
    q, a = get_input()
    for x in solve(a, q):
        print(x)

if __name__ == '__main__':
    main()

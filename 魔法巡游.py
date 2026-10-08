
from collections import defaultdict

def get_input():
    n = int(input())
    s = list(input().split())
    sd = pre_process(n, s)
    del s
    t = list(input().split())
    td = pre_process(n, t)
    del t
    return n, sd, td

def pre_process(n: int, nums: list):
    d = defaultdict(dict)

    for i in range(n):
        di = {
            '0': 0,
            '2': 0,
            '4': 0
        }
        if '0' in nums[i]:
            di['0'] += 1
        if '2' in nums[i]:
            di['2'] += 1
        if '4' in nums[i]:
            di['4'] = 1
        d[i] = di
    return d


def to_mask(di):
    """将 {'0':v,'2':v,'4':v} 字典转换为 3-bit mask"""
    mask = 0
    if di['0']: mask |= 1
    if di['2']: mask |= 2
    if di['4']: mask |= 4
    return mask


if __name__ == "__main__":
    n, sd, td = get_input()

    # 预计算每块石头的共鸣 mask
    s_masks = [to_mask(sd[i]) for i in range(n)]
    t_masks = [to_mask(td[i]) for i in range(n)]

    NEG = -10**9
    best_s = [NEG] * 8  # best_s[mask] = 以该 mask 的 s 石结尾的最长序列
    best_t = [NEG] * 8  # best_t[mask] = 以该 mask 的 t 石结尾的最长序列

    ans = 0
    for k in range(n):
        ms, mt = s_masks[k], t_masks[k]

        # dp_s: 以 s[k] 结尾的最长序列，小蓝先手可以直接开局
        dp_s = 1
        if ms:
            for m in range(8):
                if m & ms:
                    dp_s = max(dp_s, best_t[m] + 1)

        # dp_t: 以 t[k] 结尾的最长序列，必须接在某个 s[i] 后 (i<k)
        dp_t = NEG
        if mt:
            for m in range(8):
                if m & mt:
                    dp_t = max(dp_t, best_s[m] + 1)

        # 更新全局最优
        best_s[ms] = max(best_s[ms], dp_s)
        if dp_t > 0:
            best_t[mt] = max(best_t[mt], dp_t)

        ans = max(ans, dp_s, dp_t)

    print(ans)
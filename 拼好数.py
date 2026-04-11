
def get_input() -> tuple[int, list]:
    n = int(input())
    a = list(map(str, input().split()))
    return n, a


def calculate(n: int, a: list) -> int:
    sixes = [s.count('6') for s in a]

    # 1. 单独成好数
    ans = sum(1 for c in sixes if c >= 6)
    rem = sorted(c for c in sixes if c < 6)
    m = len(rem)

    if m == 0:
        return ans

    # 2. 贪心配对（双指针）
    paired = [False] * m
    l, r = 0, m - 1
    while l < r:
        if rem[l] + rem[r] >= 6:
            paired[l] = paired[r] = True
            ans += 1
            l += 1
            r -= 1
        else:
            l += 1

    # 3. 贪心三合一
    pool = sorted((rem[i] for i in range(m) if not paired[i]), reverse=True)
    i = 0
    while i + 2 < len(pool):
        if pool[i] + pool[i + 1] + pool[i + 2] >= 6:
            ans += 1
            i += 3
        else:
            break

    return ans


if __name__ == '__main__':
    print(calculate(*get_input()))
from functools import cache


def get_input():
    n, m = map(int, input().split())
    return n, m


def calculate_sum(n, m):
    s = str(n)
    n_len = len(s)

    @cache
    def dp(pos, pre, acc, tight):
        if pos == n_len:
            return 1

        limit = int(s[pos]) if tight else 9
        count = 0
        for d in range(limit + 1):
            new_tight = tight and (d == limit)
            if pre == -1 and d == 0:
                count += dp(pos + 1, -1, 0, new_tight)
            else:
                diff = 0 if pre == -1 else abs(pre - d)
                if acc + diff <= m:
                    count += dp(pos + 1, d, acc + diff, new_tight)
        return count

    return dp(0, -1, 0, True)


if __name__ == "__main__":
    n, m = get_input()
    print(calculate_sum(n, m))

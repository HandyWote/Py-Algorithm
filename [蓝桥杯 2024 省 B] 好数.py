n = int(input())
if n == 0:
    print(0)
else:
    s = str(n)
    m = len(s)
    precompute = 0
    for k in range(1, m):
        if k % 2 == 1:
            precompute += 5 ** k
        else:
            precompute += 4 * 5 ** (k - 1)
    
    from functools import lru_cache
    
    @lru_cache(maxsize=None)
    def dp(pos, tight):
        if pos == m:
            return 1
        i = m - pos
        current_max = int(s[pos]) if tight else 9
        total = 0
        
        if i % 2 == 1:  # 当前位必须是奇数
            choices = [1, 3, 5, 7, 9]
            for d in choices:
                if d > current_max:
                    continue
                new_tight = tight and (d == int(s[pos]))
                total += dp(pos + 1, new_tight)
        else:  # 当前位必须是偶数
            if pos == 0:
                choices = [2, 4, 6, 8]
            else:
                choices = [0, 2, 4, 6, 8]
            for d in choices:
                if d > current_max:
                    continue
                new_tight = tight and (d == int(s[pos]))
                total += dp(pos + 1, new_tight)
        return total
    
    equal_part = dp(0, True)
    print(precompute + equal_part)